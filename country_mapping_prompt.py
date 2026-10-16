"""Build the JSON request for preparedness-exposure country assignment.

The build_prompt function preserves the original country-expansion prompt.
The command-line wrapper renders a request payload using the standard library.
"""

import argparse
import json
from pathlib import Path
import re
import sys

SYSTEM_PROMPT = 'You label country involvement in global shipping risk events. Output valid JSON only.'


def build_prompt(events):
    compact_events = []
    for e in events:
        compact_events.append(
            {
                "original_id": e["original_id"],
                "report_date": e["report_date"],
                "article_title": e["article_title"],
                "risk_event_title": e["risk_event_title"],
                "risk_event_month": e["risk_event_month"],
                "risk_L1": e["risk_L1"],
                "risk_L2": e["risk_L2"],
                "existing_occurrence_country": e["existing_occurrence_country"],
                "existing_affected_country": e["existing_affected_country"],
                "event_text": e["event_text"],
            }
        )
    return (
        "You are a structured annotator for global shipping and supply-chain risk events.\n"
        "Classify country involvement into three different layers for each event.\n"
        "Return STRICT JSON only, no markdown, no explanation outside JSON.\n\n"
        "Output schema:\n"
        '{"events":[{"original_id":"...","occurrence_countries_strict":["..."],'
        '"direct_affected_countries":["..."],"shipping_network_affected_countries":["..."],'
        '"country_evidence":{"occurrence":"...","direct_affected":"...","network_affected":"..."}}]}\n\n'
        "Definitions:\n"
        "1. occurrence_countries_strict: countries where the risk event physically, legally, politically, or operationally occurs. "
        "Use the supplied existing_occurrence_country unless the text clearly contradicts it.\n"
        "2. direct_affected_countries: countries explicitly mentioned or directly implied by the article as being affected. "
        "This should be evidence-based and conservative.\n"
        "3. shipping_network_affected_countries: countries likely affected through international shipping networks, trade lanes, "
        "container flows, dry bulk/tanker routes, canal/strait chokepoints, port substitutions, sanctions, insurance, freight rates, "
        "or rerouting. This field may infer beyond explicit country mentions, but must remain plausible for the event. Return at most 20 countries.\n\n"
        "Country rules:\n"
        "- Use standard English country names only, e.g. United States, China, Russia, United Kingdom, South Korea.\n"
        "- Do not output ports, cities, canals, seas, oceans, continents, or regions such as Europe, Asia, Global, Red Sea, Suez Canal.\n"
        "- If a region is affected, infer the most relevant countries, not the region name.\n"
        "- If no country can be inferred for a field, return [\"Unknown\"].\n"
        "- Keep occurrence_countries_strict narrow; keep shipping_network_affected_countries broad enough to represent global maritime spillovers.\n"
        "- For a country-level domestic port disruption, include major trading partners only when the text or route context supports spillover.\n"
        "- country_evidence should be short. For network_affected, state the shipping logic briefly, not a long explanation.\n\n"
        "Input events JSON:\n"
        + json.dumps(compact_events, ensure_ascii=False)
    )


def prepare_events(events, max_input_chars=2200):
    """Apply the original whitespace normalization and text-length cap."""
    if max_input_chars < 1:
        raise ValueError("max_input_chars must be positive")
    prepared = []
    for event in events:
        item = dict(event)
        value = item.get("event_text")
        text = "" if value is None else str(value)
        text = re.sub(r"\s+", " ", text).strip()
        if len(text) > max_input_chars:
            text = text[:max_input_chars] + " ..."
        item["event_text"] = text
        prepared.append(item)
    return prepared


def build_request(events, model, max_tokens=10000, max_input_chars=2200):
    """Construct the original request format with an explicit model identifier."""
    if not isinstance(model, str) or not model.strip():
        raise ValueError("Supply the model identifier used for the run")
    if max_tokens < 1:
        raise ValueError("max_tokens must be positive")
    return {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_prompt(prepare_events(events, max_input_chars))},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.0,
        "max_tokens": max_tokens,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="UTF-8 JSON list of event records")
    parser.add_argument("--model", required=True, help="Actual model identifier for the run")
    parser.add_argument("--output", type=Path, help="Write the request payload to this file")
    parser.add_argument("--max-input-chars", type=int, default=2200)
    parser.add_argument("--max-tokens", type=int, default=10000)
    args = parser.parse_args()
    events = json.loads(args.input.read_text(encoding="utf-8-sig"))
    if not isinstance(events, list) or not all(isinstance(item, dict) for item in events):
        parser.error("Input must be a JSON list of event objects")
    try:
        payload = build_request(events, args.model, args.max_tokens, args.max_input_chars)
    except (ValueError, KeyError, TypeError) as error:
        parser.error(str(error))
    result = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    else:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()

# ANCHOR preparedness-exposure mapping prompt

Prompt construction and JSON request-format code for assigning three country roles in shipping-risk records:

- Reported risk origin: `occurrence_countries_strict`
- Documented exposure: `direct_affected_countries`
- Preparedness exposure: `shipping_network_affected_countries`

The preparedness field permits inference through shipping networks, trade lanes, chokepoints, rerouting, port substitution and related commercial mechanisms. It identifies candidate countries for preparedness analysis. Inclusion does not establish a reported consequence or realised loss.

## Files

- `country_mapping_prompt.py`: original prompt-construction function and a standalone request-rendering wrapper.
- `system_prompt.txt`: complete system instruction.
- `user_prompt_template.txt`: complete user template, with a placeholder for the serialized input batch.
- `input_template.json`: input-field template. Replace its bracketed placeholders before using it with actual records.

The rule table, processing workflow and archived output examples are documented in the accompanying Supplementary Information.

## Usage

Python 3.9 or later is sufficient; the module uses only the standard library.

```bash
python country_mapping_prompt.py --input input_template.json --model YOUR_ACTUAL_MODEL_ID --output request.json
```

This command writes a JSON request payload. It does not call a model API.

The model identifier is supplied explicitly. The request uses `temperature=0.0` and JSON-object response formatting. The default text-length cap is 2,200 characters and the default output-token limit is 10,000:

```bash
python country_mapping_prompt.py --input YOUR_INPUT.json --model YOUR_ACTUAL_MODEL_ID --max-input-chars 2200 --max-tokens 10000 --output request.json
```

The wrapper collapses whitespace in `event_text` and appends ` ...` after truncation. The `build_prompt` function preserves the original prompt text and input-field selection. File loading, command-line options and request rendering were added for this standalone release.

Record the actual model version, call dates and parameter overrides when running the mapping. Fixed prompts and zero temperature do not guarantee that later hosted-model calls return identical country lists. Reconstructing the reported aggregate counts requires the corresponding frozen record-level outputs and aggregation procedure.

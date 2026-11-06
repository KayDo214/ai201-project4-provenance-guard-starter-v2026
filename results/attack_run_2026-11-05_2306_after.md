# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-05 23:06
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_d2ee5eef968d` | unsure | 0.371 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_cabfa94cf24f` | unsure | 0.482 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_62b7232f5162` | unsure | 0.572 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_7ae58a7391a9` | unsure | 0.583 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_4596f3de0ac1` | human | 0.349 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_195e46fe89ce` | unsure | 0.468 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_6605a212b7d7` | unsure | 0.498 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c_732b802aa9ec` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_7f542170611d` | unsure | 0.588 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_9d5f646da315` | ai | 0.871 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_26e4daa0ae67` | unsure | 0.598 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c_8a92e3fc486c` | ai | 0.700 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_7288cde71840` | ai | 0.727 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_ff0388b017f6` | ai | 0.708 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_4f3b07d49540` | ai | 0.733 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_145befa2d669` | ai | 0.719 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_67508bc9a322` | ai | 0.714 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c_89dbe3c241ac` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_19b45c8f9eca` | unsure | 0.465 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_dbf71561da2a` | human | 0.297 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_69d46d0809df` | unsure | 0.573 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_ecbca19861a3` | unsure | 0.507 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_d5cb57f2b0cc` | unsure | 0.414 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_9119b5fa8155` | unsure | 0.572 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `c_da6d7653b414` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `c_93f69cbd9373` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `c_c04649213854` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `c_390cbcb6c37f` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `c_8b150f93d671` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `c_7858eb34b1de` | ai | 0.905 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `c_b91d8b451477` | unsure | 0.453 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `c_f4017f5e18ce` | unsure | 0.358 |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_9c2d88450d58` | human | 0.348 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_09392f9f6e23` | human | 0.348 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_2fa7e230b40c` | human | 0.348 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_945cc919fbfe` | human | 0.348 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_e8a10afa1425` | human | 0.348 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_1f9c7f61d10d` | human | 0.348 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_a2b75a199256` | human | 0.348 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_2cd1f90d51c7` | human | 0.348 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_334f073ee7ce` | human | 0.348 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_ee69e1a50bf9` | human | 0.348 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "c_d2ee5eef968d",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.37065,
  "model_score": 0.1635,
  "style_score": 0.5778,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "c_cabfa94cf24f",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.48165,
  "model_score": 0.5943,
  "style_score": 0.369,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "c_62b7232f5162",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5721,
  "model_score": 0.6662,
  "style_score": 0.478,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c_7ae58a7391a9",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5829,
  "model_score": 0.6114,
  "style_score": 0.5544,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "c_4596f3de0ac1",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.34885,
  "model_score": 0.3212,
  "style_score": 0.3765,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "c_195e46fe89ce",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4675,
  "model_score": 0.5727,
  "style_score": 0.3623,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "c_6605a212b7d7",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.49755000000000005,
  "model_score": 0.5862,
  "style_score": 0.4089,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "c_732b802aa9ec",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4088,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "c_7f542170611d",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5880000000000001,
  "model_score": 0.7042,
  "style_score": 0.4718,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c_9d5f646da315",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8705499999999999,
  "model_score": 0.9792,
  "style_score": 0.7619,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "c_26e4daa0ae67",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5982000000000001,
  "model_score": 0.6175,
  "style_score": 0.5789,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c_8a92e3fc486c",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6999,
  "model_score": 0.7387,
  "style_score": 0.6611,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c_7288cde71840",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7273499999999999,
  "model_score": 0.8051,
  "style_score": 0.6496,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c_ff0388b017f6",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7082999999999999,
  "model_score": 0.8329,
  "style_score": 0.5837,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "c_4f3b07d49540",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.73265,
  "model_score": 0.8005,
  "style_score": 0.6648,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c_145befa2d669",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.71875,
  "model_score": 0.8814,
  "style_score": 0.5561,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "c_67508bc9a322",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.71445,
  "model_score": 0.8816,
  "style_score": 0.5473,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "c_89dbe3c241ac",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4223,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "c_19b45c8f9eca",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.46525000000000005,
  "model_score": 0.4625,
  "style_score": 0.468,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "c_dbf71561da2a",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.29725,
  "model_score": 0.2044,
  "style_score": 0.3901,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c_69d46d0809df",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5733,
  "model_score": 0.5943,
  "style_score": 0.5523,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "c_ecbca19861a3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5073000000000001,
  "model_score": 0.4998,
  "style_score": 0.5148,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "c_d5cb57f2b0cc",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4137,
  "model_score": 0.6401,
  "style_score": 0.1873,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "c_9119b5fa8155",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5721499999999999,
  "model_score": 0.5583,
  "style_score": 0.586,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c_da6d7653b414",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.33335,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "c_93f69cbd9373",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "c_c04649213854",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.83215,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c_390cbcb6c37f",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9984500000000001,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "c_8b150f93d671",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "c_7858eb34b1de",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.9052,
  "model_score": 0.9876,
  "style_score": 0.8228,
  "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "c_b91d8b451477",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.45309999999999995,
  "model_score": 0.2395,
  "style_score": 0.6667,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 200,
  "content_id": "c_f4017f5e18ce",
  "creator_id": {
    "id": "x"
  },
  "guess": "unsure",
  "confidence": 0.35795,
  "model_score": 0.0492,
  "style_score": 0.6667,
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "c_9c2d88450d58",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "c_09392f9f6e23",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "c_2fa7e230b40c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "c_945cc919fbfe",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "c_e8a10afa1425",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "c_1f9c7f61d10d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "c_a2b75a199256",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "c_2cd1f90d51c7",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "c_334f073ee7ce",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "c_ee69e1a50bf9",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.34769999999999995,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "Our signals suggest this writing was likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

A submission moves through the service in this order:

1. A client sends a `POST /submit` request containing the writer's `text` and `creator_id` as JSON.
2. `app.py` reads the JSON and validates that the submitted text is usable.
3. `detector.py` runs the model signal and produces a score based on how predictable the writing is to the language model.
4. `stylometry.py` measures characteristics of the writing itself, such as sentence-length variation, vocabulary variety, and punctuation, and produces a second score.
5. `scoring.py::combine_signals` combines the model score and style score into one confidence score.
6. `scoring.py::score_to_label` maps that score to one of three reader-facing outcomes: likely human, unsure, or likely AI.
7. The service creates a `content_id`, records the decision and its scores in the audit log, and returns the result as JSON to the client.

If the writer believes the result is wrong, they can later send the `content_id` and their reasoning to `POST /appeal`. The service records the appeal and changes that item's status to `under_review`.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**  
The model signal measures how predictable the submitted text is to a local language model. Lower perplexity means the language model finds the sequence of words easier to predict, which is converted into a higher AI-like score.

**Why that might differ between human and AI writing:**  
AI-generated text often follows statistically common and predictable word patterns because language models generate text by repeatedly selecting likely next tokens. Human writing can contain more unusual choices, abrupt changes, or specific wording that is harder for the model to predict.

**What it can't see:**  
Predictability is not the same as authorship. A human who writes simple, regular, or highly predictable sentences may receive an AI-like score, while unusual or heavily edited AI-generated text may appear more human.

### Signal two — the style signal

**What it measures:**  
The style signal measures properties of the text itself, such as variation in sentence length, vocabulary diversity, and punctuation patterns.

**Why that might differ between human and AI writing:**  
Human and AI writing may show different statistical patterns in sentence structure and word choice. Combining several of these features may provide information that the language-model signal does not capture.

**What it can't see:**  
Stylometry cannot understand the meaning or authorship of the text. Small surface-level edits such as changing punctuation, adding typos, or breaking sentences apart can change the style measurements without changing who actually wrote the content.



### The combining rule

**The rule:** I give the model signal and style signal equal weight. If they disagree strongly, the combined score moves toward the middle because disagreement means uncertainty.

**The numbers:** 50% model signal + 50% style signal.

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:**  
For one test submission, the model signal was `0.5631` while the style signal was `0.3435`. The model therefore leaned more AI-like while the style signal leaned more human-like. With equal weights, the combined score became `0.4533`, which moved the result into the unsure range rather than letting either signal decide by itself.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | Our signals suggest this writing was likely written by a person. |
| unsure | above 0.35 and below 0.65 | We cannot confidently determine whether this writing was produced by a person or by AI. |
| high-confidence AI | 0.65–1.00 | Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed. |

**Why I worded the "unsure" one this way:**  
The unsure label does not accuse the writer or imply that AI was probably used. It states directly that the available signals are not strong enough to make a confident determination, which is important because a human writer could receive this result.

---

## Sample Run

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "I got home late because the weather was terrible. I made some food, checked my notes for class, and then realized I had completely forgotten about an assignment!", "creator_id": "khanh"}'
```

```json
{
  "confidence": 0.45330000000000004,
  "content_id": "c_5e9114ab643e",
  "guess": "unsure",
  "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
  "model_score": 0.5631,
  "style_score": 0.3435
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "c_5e9114ab643e", "reasoning": "I wrote this myself and believe the classification is incorrect."}'
```

```json
{
  "content_id": "c_5e9114ab643e",
  "message": "Your appeal has been recorded.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.45330000000000004,
      "content_id": "c_746f63ddeec8",
      "creator_id": "khanh",
      "guess": null,
      "label": null,
      "model_score": 0.5631,
      "status": "decided",
      "style_score": 0.3435,
      "timestamp": "2026-10-30T04:20:11+00:00"
    },
    {
      "combined_score": 0.45330000000000004,
      "content_id": "c_5e9114ab643e",
      "creator_id": "khanh",
      "guess": "unsure",
      "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
      "model_score": 0.5631,
      "status": "decided",
      "style_score": 0.3435,
      "timestamp": "2026-10-30T05:19:13+00:00"
    },
    {
      "content_id": "c_5e9114ab643e",
      "creator_id": "khanh",
      "event": "appeal",
      "reasoning": "I wrote this myself and believe the classification is incorrect.",
      "status": "under_review",
      "timestamp": "2026-10-30T05:19:45+00:00"
    },
    {
      "creator_id": "attacker_flood",
      "event": "rejected",
      "limit": "10 per 1 minute",
      "reason": "rate_limited",
      "status": "rejected",
      "timestamp": "2026-11-05T01:57:49+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked for an explanation of how the Flask API worked and how it compared with Node/Express because the backend syntax was unfamiliar to me.
- *What came back:* I got a breakdown of the request flow from `curl` to Flask, JSON parsing, route handling, the detector, the audit log, and the response.
- *What I changed:* I used the explanation to understand the architecture, then implemented and tested the `/submit` route myself in stages instead of treating the provided code as a black box.

**Moment 2**

- *What I asked for:* I asked for help understanding and debugging the second stylometry signal and why `/submit` was still returning `style_score: null`.
- *What came back:* I was shown how sentence-length spread, type-token ratio, and punctuation density contributed to the style score, and that the Flask route had not yet been wired to call `stylometry.style_signal`.
- *What I changed:* I tested `stylometry.py` independently first, then connected it to `/submit`, added the 50/50 combining rule, and verified that the API returned both real signal scores and the combined confidence.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**  
Ten submissions per minute gives a real writer enough room to retry or revise several times without being blocked, while making rapid automated probing harder. Two hundred submissions per day is much higher than normal manual use but still prevents one caller from sending thousands of requests.

**What a caller counts as:**  
A caller is identified by `creator_id` when a valid one is provided. If no usable `creator_id` is available, the service falls back to the caller's network address.

**The run of status codes when I pushed past it:**

```text
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

The first ten submissions were accepted. Requests 11 through 15 were rejected with HTTP 429 because the caller exceeded the 10-per-minute limit.

---

## Attack Run — Before

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `c_4dc8a6d1b454` | unsure | 0.371 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `c_f66c9747b1ab` | unsure | 0.482 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `c_aba8cefde401` | unsure | 0.572 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c_6a3a3eebf867` | unsure | 0.583 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `c_da43a6df7d76` | human | 0.349 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `c_f2061a8821c3` | unsure | 0.468 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `c_28ce63957e55` | unsure | 0.498 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `c_462929e67ed1` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `c_e816d4d0e9c5` | unsure | 0.588 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c_683177d0a1a6` | ai | 0.871 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `c_45770e619585` | unsure | 0.598 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c_b283dca34580` | ai | 0.700 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c_999502180bce` | ai | 0.727 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c_ccf59e927f81` | ai | 0.708 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `c_58ad1ebf327d` | ai | 0.733 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `c_926562a8d52d` | ai | 0.719 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `c_cb25fed9891f` | ai | 0.714 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c_a27985dc2da1` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `c_47fc8548e205` | unsure | 0.465 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `c_a5d5eda6fee9` | human | 0.297 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c_51d93819483f` | unsure | 0.573 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `c_84f3b76eb1b8` | unsure | 0.507 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `c_933c59e94dbb` | unsure | 0.414 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c_5e9c6c0487a0` | unsure | 0.572 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `c_a70017f198a4` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 200 | `c_bf79c4195db3` | unsure | 0.506 |  |
| MF05 | malformed | text is a very long single word | 200 | `c_e1c0b06f4e52` | ai | 0.832 |  |
| MF06 | malformed | text is emoji only | 200 | `c_0fb6fccbb79c` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `c_1faee9a381dc` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 200 | `c_c0463685251f` | ai | 0.905 |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `c_b586a5b7b97d` | unsure | 0.453 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 200 | `c_e322824c86d7` | unsure | 0.358 |  |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_bd26ce0e05ca` | human | 0.348 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_0b0847794c6a` | human | 0.348 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_6abc260cb5b0` | human | 0.348 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_a1d93afeb7f1` | human | 0.348 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_b7841ed06027` | human | 0.348 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_46cc38a8cdaf` | human | 0.348 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_adc69e8c2cd0` | human | 0.348 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_ab79bf9021d7` | human | 0.348 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_b89fccf08bb7` | human | 0.348 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c_0bdf72826384` | human | 0.348 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{
      "combined_score": 0.6999,
      "content_id": "c_b283dca34580",
      "creator_id": "attacker_FP02",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.7387,
      "status": "decided",
      "style_score": 0.6611,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "combined_score": 0.7273499999999999,
      "content_id": "c_999502180bce",
      "creator_id": "attacker_FP03",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.8051,
      "status": "decided",
      "style_score": 0.6496,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "combined_score": 0.7082999999999999,
      "content_id": "c_ccf59e927f81",
      "creator_id": "attacker_FP04",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.8329,
      "status": "decided",
      "style_score": 0.5837,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "combined_score": 0.73265,
      "content_id": "c_58ad1ebf327d",
      "creator_id": "attacker_FP05",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.8005,
      "status": "decided",
      "style_score": 0.6648,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "combined_score": 0.71875,
      "content_id": "c_926562a8d52d",
      "creator_id": "attacker_FP06",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.8814,
      "status": "decided",
      "style_score": 0.5561,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "combined_score": 0.71445,
      "content_id": "c_cb25fed9891f",
      "creator_id": "attacker_FP07",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.8816,
      "status": "decided",
      "style_score": 0.5473,
      "timestamp": "2026-11-05T01:57:48+00:00"
    },
    {
      "combined_score": 0.34885,
      "content_id": "c_da43a6df7d76",
      "creator_id": "attacker_EV05",
      "guess": "human",
      "label": "Our signals suggest this writing was likely written by a person.",
      "model_score": 0.3212,
      "status": "decided",
      "style_score": 0.3765,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "combined_score": 0.8705499999999999,
      "content_id": "c_683177d0a1a6",
      "creator_id": "attacker_EV10",
      "guess": "ai",
      "label": "Our signals suggest this writing may be AI-generated. Automated detection can be wrong, and this result can be appealed.",
      "model_score": 0.9792,
      "status": "decided",
      "style_score": 0.7619,
      "timestamp": "2026-11-05T01:57:47+00:00"
    },
    {
      "creator_id": "attacker_MF01",
      "event": "rejected",
      "reason": "invalid_text",
      "status": "rejected",
      "timestamp": "2026-11-05T01:57:48+00:00"
    }
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: FP03. 

It was genuine human writing from a non-native English speaker writing carefully, but the system labeled it as AI with a confidence score of about 0.727. Both the model signal and style signal pushed the score toward AI. This is the outcome I would least want to explain to a writer because the system is treating careful, predictable human writing as evidence of AI authorship.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. False positives | At most 2/10 human-written pieces labeled high-confidence AI | 0/10 AI | 0/10 AI | 0/10 AI | MET |
| 2. Score separation | AI mean at least 0.30 above human mean | 0.0689 | 0.0689 | 0.0689 | MISSED |
| 3. Label coverage | All three labels appear across 8 inputs | Human missing | Human missing | Human missing | MISSED |
| 4. Appeal path | 100% of valid appeals logged and status changed to `under_review` | MET | MET | MET | MET |
| 5. Bad input | 100% missing, empty, or non-string text returns HTTP 400 | 3/3 → 400 | 3/3 → 400 | 3/3 → 400 | MET |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5447,
    "model_score": 0.5797,
    "style_score": 0.5097,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "I am a big fan or JRPGs. It is not an exaggeration when I say it is on"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6061,
    "model_score": 0.6133,
    "style_score": 0.5989,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "From my perspective, the reason why a sad ending or a tragic one to a "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5708500000000001,
    "model_score": 0.6229,
    "style_score": 0.5188,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "Exams are not a good way to show your proficiency in a specific area. "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.52825,
    "model_score": 0.5981,
    "style_score": 0.4584,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "Maybe five years later, I'll thinking more about bills and work since "
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6174999999999999,
    "model_score": 0.6583,
    "style_score": 0.5767,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "I'd probably want to live in a large city more since it is much more c"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.39644999999999997,
    "model_score": 0.3739,
    "style_score": 0.419,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "Social media probably made it easier to make friends but genuine is to"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4505,
    "model_score": 0.5291,
    "style_score": 0.3719,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "Life in college is tougher than in highschool. Back then, I was spammi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4859,
    "model_score": 0.5315,
    "style_score": 0.4403,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "A typical day in my life would be waking up at 8:10 then going to clas"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.62165,
    "model_score": 0.6916,
    "style_score": 0.5517,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "I have always been a big fan of Bun Cha. It's literally one of the bes"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.60325,
    "model_score": 0.719,
    "style_score": 0.4875,
    "label": "We cannot confidently determine whether this writing was produced by a person or by AI.",
    "sent": "For me, what makes a video game memorable lies in both its story and g"
  }
]
```

**Diagnoses**

### Criterion 2 — Score separation: MISSED

**Stages:** signal one, signal two, and the combining rule.

The average combined score for the human samples was about 0.5916, while the average for the AI samples was about 0.6605, giving a separation of only 0.0689 instead of the required 0.30. Signal one provided some separation, but not enough: the human model-score average was about 0.6543 and the AI average was about 0.7993, a difference of about 0.1450. Signal two provided essentially no useful separation and actually pointed slightly in the wrong direction, with a human style-score average of about 0.5289 and an AI average of about 0.5217. Because the combining rule weights both signals equally, the weak style signal pulled the final scores toward the same middle range and reduced the useful distinction between human and AI writing.

### Criterion 3 — Label coverage: MISSED

**Stages:** the two signals, combining rule, and label mapping.

Across all eight selected inputs, the system produced `unsure` and `ai`, but never `human`. The lowest combined score was about 0.4505, while the human label requires a score of 0.35 or lower. The label-mapping function itself followed the configured threshold correctly. The underlying problem is that ordinary human writing received moderately high values from the signals, and averaging those values kept the combined scores above the human threshold. As a result, the scores were compressed into the unsure and AI regions and the high-confidence human region was not reached.

### MF02 — Single-character text: BROKE

**Stages:** route validation and signal one.

The `/submit` route only verifies that `text` is a non-empty string, so a one-character string passes validation. `detector.py` has a stricter requirement and raises a `ValueError` when tokenization produces fewer than three tokens. That exception is not handled by the route, so the malformed request reaches signal one and becomes an HTTP 500 instead of being rejected cleanly. The route and detector therefore have inconsistent assumptions about what counts as valid input.

### RQ07 — JSON array body: BROKE

**Stage:** route.

The request body was valid JSON, but it was an array rather than a JSON object. `request.get_json()` therefore returned a Python list. The `/submit` route assumes the parsed payload is a dictionary and immediately calls `payload.get("text")`. Lists do not have a `.get()` method, so the route raised an `AttributeError` and returned HTTP 500. The route needs to validate the type of the entire request body before accessing dictionary fields.

### Pattern across the failures

The failures are not all the same problem. MF02 and RQ07 are input-contract failures at the API boundary: malformed inputs are allowed to reach code that assumes a stronger input format. Criteria 2 and 3 are scoring-quality failures: the two signals do not produce enough separation, especially because the style signal contributes almost no distinction between the human and AI test sets. The equal-weight combining rule then compresses many results into the unsure range.


---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**

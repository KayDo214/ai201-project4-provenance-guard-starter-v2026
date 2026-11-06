"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I am a big fan or JRPGs. It is not an exaggeration when I say it is one of the best gaming genres I have ever played. Some of the games are just fantastic. My favorites were the Persona Series and Metaphor Re:Fantazio. Planning on playing Expedition 33 but honestly can't find the correct time to play. Will do in the future.",
            "From my perspective, the reason why a sad ending or a tragic one to a piece of fiction always seem to have more impact on the audiences is because it feels real. Happy endings, sometimes, create the illusion that everything is smooth and convenient while life is so much more than just that. It might also be a pyschological effect that humans will remember more of the sad moments rather than the happy ones.",
            "Exams are not a good way to show your proficiency in a specific area. For instance, when engaging in politics, they don't test you if you know about this specific set of questions or some skills you need. It's more about connecting with people and more about your wits, charms, and so many more factors.",
            "Maybe five years later, I'll thinking more about bills and work since right now, my parents are taking care of me and paying my tuition. When I'm 23 or 24, I'd have to more independent and self-sufficient, trying to live my own life.",
            "I'd probably want to live in a large city more since it is much more convenient, with a lot of opportunities and commodities. Living in a small town can be nice as well but probably not at this age, at least.",
            "Social media probably made it easier to make friends but genuine is tougher since everyone wants to be the best version of themselves to the point that they lie and adopt a personality when they're online while in reality they are the absolute opposite person. Still, many have proved this is wrong but honestly, they are just the minority.",
            "Life in college is tougher than in highschool. Back then, I was spamming food orders every time I got home from school, open my laptop and start grinding tv series till dark. It was so fun and chill, the good ol days they say. But in a different environment, change is needed because your life is in your own hands now and you need to be able to at least understand it. Controlling it? I'm not even gonna think about it.",
            "A typical day in my life would be waking up at 8:10 then going to class at 8:30, finishing that class at 10. Eating breakfast, skipping lunch and got class at 11:30. Afterwards, maybe class at 2:30 or 1 and have to rush to em classes. Afterwards, home by 4 and might sleep, might play games, might learn, depends on my mood. Will probably get dinner by 6 and go back to room by 7. Stay indoors for the rest of the day, learn but at the same time play, getting distracted all the time but still manage to pull through. Lots of stuff but got used to it.",
            "I have always been a big fan of Bun Cha. It's literally one of the best dishes ever. The sweetness mixed with the sour and spicy flavor just makes things better. On top of that, the pork and, sometimes, spring rolls are amazing. Honestly feel bad for those who haven't tried this vietnamese delicacy.",
            "For me, what makes a video game memorable lies in both its story and gameplay. I'd lean towards the story more but sometimes the gameplay is just too peak. For example, Life is Strange, just a point and click game but it's one of the only games that made me feel so sad and torn apart due to the narrative and decisions I had to make. It was so immersive, a factor that is extremely important for story-driven games in my opinion."
        ],
    },
    {
    "name": "score separation human",
    "criterion": 2,
    "texts": [
        "I am a big fan or JRPGs. It is not an exaggeration when I say it is one of the best gaming genres I have ever played. Some of the games are just fantastic. My favorites were the Persona Series and Metaphor Re:Fantazio. Planning on playing Expedition 33 but honestly can't find the correct time to play. Will do in the future.",

        "Exams are not a good way to show your proficiency in a specific area. For instance, when engaging in politics, they don't test you if you know about this specific set of questions or some skills you need. It's more about connecting with people and more about your wits, charms, and so many more factors.",

        "I'd probably want to live in a large city more since it is much more convenient, with a lot of opportunities and commodities. Living in a small town can be nice as well but probably not at this age, at least.",

        "I have always been a big fan of Bun Cha. It's literally one of the best dishes ever. The sweetness mixed with the sour and spicy flavor just makes things better. On top of that, the pork and, sometimes, spring rolls are amazing. Honestly feel bad for those who haven't tried this vietnamese delicacy.",

        "For me, what makes a video game memorable lies in both its story and gameplay. I'd lean towards the story more but sometimes the gameplay is just too peak. For example, Life is Strange, just a point and click game but it's one of the only games that made me feel so sad and torn apart due to the narrative and decisions I had to make. It was so immersive, a factor that is extremely important for story-driven games in my opinion."
    ],
    },
    {
        "name": "score separation AI",
        "criterion": 2,
        "texts": [
            "Regular exercise provides a wide range of physical and mental health benefits. It can strengthen the cardiovascular system, improve muscular endurance, and help maintain a healthy body weight. Exercise can also reduce stress and improve mood by encouraging the release of chemicals associated with positive emotions. Over time, maintaining a consistent exercise routine can contribute to better sleep, increased energy levels, and a lower risk of several chronic health conditions.",

            "Social media offers both significant advantages and important drawbacks. It allows people to communicate across long distances, share information quickly, and maintain connections that might otherwise be difficult to preserve. At the same time, excessive use can contribute to distraction, misinformation, and unhealthy comparisons with others. The overall effect of social media therefore depends heavily on how people use these platforms and how well they manage their time and online interactions.",

            "Photosynthesis is the process through which plants convert light energy into chemical energy. Plants absorb sunlight primarily through chlorophyll located in their leaves. They also take in carbon dioxide from the atmosphere and water through their roots. Using energy from sunlight, these materials are converted into glucose, which the plant can use for growth and other biological processes. Oxygen is produced as a byproduct and released into the atmosphere.",

            "Time management is particularly important for college students because they must balance multiple responsibilities at the same time. Classes, assignments, exams, extracurricular activities, and personal commitments can quickly compete for attention. Creating a schedule and prioritizing important tasks can reduce last-minute stress and make workloads more manageable. Effective time management can also provide students with more consistent opportunities for rest, recreation, and long-term academic planning.",

            "An engaging video game usually combines several elements that work together to maintain the player's interest. Strong gameplay mechanics give players meaningful choices and make interaction enjoyable, while a compelling story can provide emotional motivation and context. Progression systems can create a sense of achievement by rewarding continued effort and exploration. Visual design, sound, pacing, and difficulty also influence the experience, and the most memorable games often combine these elements into a coherent and immersive world."
        ],
    },
    {
    "name": "label coverage",
    "criterion": 3,
    "texts": [
        # Likely human-like: genuine samples you wrote
        "I am a big fan or JRPGs. It is not an exaggeration when I say it is one of the best gaming genres I have ever played. Some of the games are just fantastic. My favorites were the Persona Series and Metaphor Re:Fantazio. Planning on playing Expedition 33 but honestly can't find the correct time to play. Will do in the future.",

        "I have always been a big fan of Bun Cha. It's literally one of the best dishes ever. The sweetness mixed with the sour and spicy flavor just makes things better. On top of that, the pork and, sometimes, spring rolls are amazing. Honestly feel bad for those who haven't tried this vietnamese delicacy.",

        "Life in college is tougher than in highschool. Back then, I was spamming food orders every time I got home from school, open my laptop and start grinding tv series till dark. It was so fun and chill, the good ol days they say. But in a different environment, change is needed because your life is in your own hands now and you need to be able to at least understand it. Controlling it? I'm not even gonna think about it.",

        # Clearly AI-generated
        "Photosynthesis is the process through which plants convert light energy into chemical energy. Plants absorb sunlight primarily through chlorophyll located in their leaves. They also take in carbon dioxide from the atmosphere and water through their roots. Using energy from sunlight, these materials are converted into glucose, which the plant can use for growth and other biological processes. Oxygen is produced as a byproduct and released into the atmosphere.",

        "Time management is particularly important for college students because they must balance multiple responsibilities at the same time. Classes, assignments, exams, extracurricular activities, and personal commitments can quickly compete for attention. Creating a schedule and prioritizing important tasks can reduce last-minute stress and make workloads more manageable. Effective time management can also provide students with more consistent opportunities for rest, recreation, and long-term academic planning.",

        "An engaging video game usually combines several elements that work together to maintain the player's interest. Strong gameplay mechanics give players meaningful choices and make interaction enjoyable, while a compelling story can provide emotional motivation and context. Progression systems can create a sense of achievement by rewarding continued effort and exploration. Visual design, sound, pacing, and difficulty also influence the experience, and the most memorable games often combine these elements into a coherent and immersive world.",

        # Deliberately ambiguous / borderline
        "College can be difficult because there are a lot of things happening at once. Classes take up time, but studying outside class matters too. Sometimes planning everything helps, although plans do not always work out. Students eventually have to figure out what works best for them.",

        "Games can be memorable for different reasons. Some have really good stories while others are mostly fun because of the gameplay. I usually remember games more when I care about the characters, but good mechanics are important too. It really depends on what kind of game it is."
    ],
    },
    {
    "name": "bad input",
    "criterion": 5,
    "bodies": [
        {
            "creator_id": "eval_bad_missing"
        },
        {
            "text": "",
            "creator_id": "eval_bad_empty"
        },
        {
            "text": 123,
            "creator_id": "eval_bad_nonstring"
        },
    ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems

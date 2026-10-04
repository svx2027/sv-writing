# Hinglish

Version 1. None of the three source skills covers Hindi or Hinglish, so Claude wrote this file from general knowledge of how Hinglish is spoken and written online. Treat every rule here as a starting default. SV's samples and feedback override it, and the retro loop should replace guesses with evidence quickly.

## How real Hinglish works

Hinglish here means Hindi and English mixed in one piece, written in Roman script. People switch at natural points: English for industry terms, product names, numbers and many nouns; Hindi for feelings, reactions, connecting words, everyday verbs, emphasis and punchlines. A Hinglish line should sound like something SV would say out loud on a call.

Defaults until samples say otherwise:

1. Script: Roman. Devanagari only when SV writes it.
2. Industry terms stay in English: views, CTR, retention, watch time, thumbnail, title, hook, upload, Shorts, niche, brand deal, audience, analytics, subscribers.
3. Spelling: one spelling per word for the whole piece. Until samples show SV's spellings, use hai, nahi, kya, toh, kyunki, zyada and pe.
4. Register: one form of "you" for the whole piece (aap, tum or tu), the one SV uses with this audience.

## Hinglish forms of the core tells

Same tiers and fixes as references/patterns.md.

#1 Binary contrasts (hard rule):
> Ye sirf ek video nahi hai, ye ek emotion hai.
> Baat views ki nahi hai, baat watch time ki hai.
> Problem algorithm nahi hai. Problem packaging hai.

Fix: say Y. "Problem packaging mein hai." A plain comparison is fine: "Watch time views se zyada matter karta hai."

#2 Closers and crutches: "Bas.", "Khatam.", "Point.", "Dobara padho.", "Ye baat yaad rakhna.", "Samjhe?"

#3 Kickers and sayings: "Aur yahi hai asli growth.", "Yahi hai success ka raaz.", "Baaki sab noise hai."

#4 Run-ups: "Ek baat bataun?", "Sach kahun toh..." as a standalone opener, "Seedhi baat:", "Suno," or "Dekhiye," as openers, "Toh chaliye shuru karte hain", "Aaiye jaante hain", "Aaj hum baat karenge..."

#5 Faux insight: "Jo koi nahi batata...", "Ye baat 99% creators nahi jaante", "Zyada tar log yahan galti karte hain" with no evidence.

#6 Rhetorical setups: "Socho agar...", "Kabhi socha hai...?", "Result? 3x views."

#7 Arguing with no one: "Mera matlab ye nahi ki...", "Galat mat samajhna, but..."

#9 Telling the reader what to think: "Ye point bahut important hai", "Isko dhyaan se padhna".

#13 Send-offs: "Ye toh bas shuruaat hai.", "Aage aur bhi bada hone wala hai!"

#32 Chatbot residue: "Umeed hai aapko ye pasand aaya hoga", "Comment mein apni raay zaroor batayein", formal "Dhanyavaad" sign-offs.

#35 Recaps: "Toh dosto, kul milakar...", "Ant mein bas itna kehna hai..."

## Hinglish-only tells

### HL1. Textbook Hindi in a casual piece

Tier: 1.
Watch for: mahatvapurn, atyant, vishesh roop se, upyog, prapt karna, avashyak, nishchit roop se, uplabdh, sambandhit, darshak, vishleshan, safalta ki kunji.
Why: Translation tools and models reach for formal, Sanskrit-heavy Hindi. People speaking Hinglish say important, use, milna, zaroori, pakka, available, audience.
Fix: Use the word SV would say on a call.
Before:
> Thumbnail ek atyant mahatvapurn tatva hai jo darshakon ko aakarshit karta hai.

After:
> Thumbnail hi decide karta hai ki log click karenge ya nahi.

### HL2. Translated industry terms

Tier: 1.
Watch for: Hindi coinages for terms creators say in English: darshak pratidhaaran (retention), click dar (CTR), sadasyata (subscription), vishay-vastu (content).
Fix: Keep the English term.
Before:
> Darshak pratidhaaran dar 40% se badhkar 55% ho gayi.

After:
> Retention 40% se 55% ho gayi.

### HL3. Switches no speaker would make

Tier: 2.
Watch for: an English post with Hindi words dropped in for flavour, or Hindi with English pasted in at odd points ("Let's do some masti and learn thumbnails", "Toh friends, let's start karte hain today's topic").
Fix: Rewrite the sentence in one flow, switching where SV would.
Before:
> Toh friends, let's start karte hain today's topic, jo hai thumbnails.

After:
> (Cut the run-up and start with the first point about thumbnails.)

### HL4. Register drift

Tier: 2.
Watch for: aap, tum and tu mixed in one piece without a reason; stiff "aap" where SV talks like a friend, or "tu" where SV is formal.
Fix: One register, SV's.
Before:
> Aap apne channel pe focus karo, tum dekhoge results.

After:
> Apne channel pe focus karo, results dikhenge.

### HL5. Glossing Hindi for an Indian audience

Tier: 2.
Watch for: English translations of Hindi words in brackets ("jugaad (a frugal fix)", "yaar (friend)") for readers who already know them.
Fix: Cut the gloss, unless SV is writing for readers who don't speak Hindi.
Before:
> Thoda jugaad (a frugal, improvised fix) lagaya.

After:
> Thoda jugaad lagaya.

### HL6. Fillers at an unnatural rate

Tier: 3.
Watch for: yaar, bhai, na, matlab, basically or literally in nearly every sentence, more often than SV uses them.
Fix: Match SV's rate from samples. Until then, use them where they carry tone, never as decoration.

### HL7. First-person verb gender

Tier: hard rule.
Hindi first-person verbs carry gender (main gaya or main gayi; main sochta hoon or main sochti hoon). Never guess SV's from a name, a photo or a draft, since a model may have written the draft. Use the form recorded in voice/profile.md. If it isn't recorded and the piece needs a first-person verb, ask in Notes (never as a question that blocks the task) and record SV's answer in a retro. Until then, use neutral constructions: "maine socha", "mujhe laga", "maine kiya", "mera plan tha".

### HL8. Script and spelling drift

Tier: 2.
Watch for: Roman and Devanagari mixed in one piece; one word spelled two ways (nahi, nahin, nai).
Fix: One script and one spelling per word.

## Hinglish intensifiers

"bahut hi", "ekdum", "sach mein", "bilkul", "itna zyada" and "really really" work like the adverbs in references/words.md: cut them when they add nothing, keep them when they carry SV's spoken rhythm. Strict mode cuts them.

## Checks before returning Hinglish

1. Would SV say every line out loud like this on a call?
2. One register, one script, one spelling per word.
3. Industry terms in English.
4. First-person verbs match voice/profile.md, or neutral constructions are used.
5. No Hinglish form of a hard-rule or tier 1 tell survived.

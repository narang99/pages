# Analysis of the high activating stories (english)

During generation, we took the vectors from the last 150 positions. In the test set, the vector alignment does happen on the tail end of the story. There seems to be a correlation at least, is the position vector encoded in our vector right now? Should we rotate it and test?

In happy stories, the proper noun seems to be always colored.

## Happy

I’m actually feeling good reading these stories. Children stories are fun.

- Lily story is basically about her loving to read books. 
  - "loved" is not colored all the times (only once out of 3 occurrences). The peak is at "Lily was so happy and excited". "happy" and "excited" are on-your-face trigger words.
  - The character and pronouns pertaining to the character are lit up
  - "bookcase" is also lit up, maybe because it is the object of happiness.
- Bear story: The bear likes nature and picnics with friends. The high tokens here are much more predictable, “enjoyed”, “happy”, “It was a wonderful day”. This story is pretty well aligned infact.
  - Again, trigger words like "happy" have high activation
  - In happy sentences, the character being happy is lit up
  - "loved" is not colored.
  - Sentence of strategizing and planning a picnic is not lit up
  - "It was a wonderful day!": the ending phrase has a peak
  - Weirdly the other peak is in the penultimate sentence on the word "and"
- Freddy the frog sees Lily painting and loves it, Lily invites him to paint with her and he is overjoyed. The emotion vector alignment is similar to the bear story, pretty good
  - trigger words: "jolly", "love"
  - "love" did not fire again.
  - "Freddy▁jumped▁up▁and▁down▁with▁excitement" is fully activated
  - "Freddy▁had▁so▁much▁fun▁that▁he" is fully activated
  - "before" in last sentence is again very high. is this a pattern? 
- Amy and Max love swinging. good alignment. There are things like “they” being consistently colored. “smiled”, “happy”, “having fun” are also colored.
  - "sunny", "smiled"
  - "▁laughing▁and▁having▁fun."
  - similar patterns, we have clearly cheerful sentences fully lighting up. "smiled" and "happy" have peak values
- Lily wants to eat something new and her mom makes a fruit salad. 
  - “They”, “mom”, “she” are colored. 
  - Sentences are colored “mom was happy to see”. “laughed”, “happy” are colored.
  - peaks at "happy", "smiled", "excited"
  - Last sentence again has a good peak.
- Bob is a jolly sheep, sings songs, helps a cold sad girl named Amy by giving her his warm wool. Critically, “Amy was sad because she was cold” is not colored at all. The moment she becomes happy, she and the rest of her sentence becomes colored. “they” and “Amy” are colored. “Bob” is weirdly not colored.

## Excited

- Lily finds a necklace and is happy about it. nouns are again colored. 
  - phrases: "Lily▁was▁so▁happy▁to▁have▁found▁the", "▁and▁skipped▁around▁her▁house,▁feeling▁very▁fancy" . "was" has stronger activation than "happy"
  - "excited", "happy" are trigger words again.
  - This is extremely similar to the happy section stories.
  - The activation patterns are also similar.
  - "loved" not colored
- Tim finds a toy car and is happy. Again “happy” is strongly colored. 
  - "▁Tim▁was▁so▁happy" is a peak. In this too, "was" has a stronger activation than "happy" itself
  - The last sentence is no longer a peak
- Freddy the frog sees Lily painting and loves it. 
  - This is the same story repeated from “happy” vector. 
  - "jumped up and down with excitement" has larger activation compared to the happy story (its a peak here)
  - "Freddy and Lily painted together" is lit up in "happy" but not in excited (normal calm happy emotions are not colored?)
- Lily loves to read books. Same story as “happy”. Very similar activation patterns again. only "excited" is much stronger than it was in the happy section


## Kind

Many times, we see that the specific words denoting kindness are not colored. Everything around is

- Sue lights up a candle her mother likes: 
  - "loved", "thoughtful" did not fire in the beginning
  - "She was happy to help" was also not firing in the beginning -> These are parts of sentences explaining her persona, the explanations are not firing up
  - The emotion vector starts firing after the act of kindness is done -> its generally about something a character does which results in someone else's happiness. 
  - "Her▁mom▁was▁so▁happy", "Sue's▁mom▁said,▁"Thank▁you,▁Sue,▁for▁being▁so▁thoughtful▁and"
  - Interestingly "▁Sue▁felt▁proud▁that▁she▁could▁help▁her▁mom" is lit up, an emotion about the character themselves (pride)
  - The act of making the candle (the act of kindesss) is relatively dark "Sue▁carefully▁lit▁the▁candle▁and▁put▁it▁on▁the▁table."

- Tom is a kind person who liked to help people but fell down and was taken to a hospital
  - This story talks about how someone is kind in an abstract sense. The word "kind" lits up. In contrast to our previous hypothesis that the vector aligns after acts of kindness, in this story, it lights up while describing someone's kind nature
  - "▁Tom▁had▁a▁big▁heart▁and▁loved▁to▁help" and "▁He▁was▁very▁generous▁and▁would▁always▁share▁his▁toys▁with▁his▁friends" are examples
  - Weirdly "▁They▁took▁him▁to▁the▁hospital▁and▁the▁doctor▁made▁him▁feel▁bette" is fully dark. The concrete act of kindness is again dark.
- A strong robot helps a little girl and they become friends. 
  - Surprisingly, specifically “happy” is not colored, everything around it is. “Robot felt sad” is also colored, although here the robot is sad for the other person (and is gonna help them in the next sentence). 
  - colored phrases: “thanking him for his kindness”, “the girl and robot became friends”, “the robot would always be there to”,  never “forgot how the robot had” (never is not colored but the kindness notion is still colored)
  - The actual act of kindness is again dark.
    - This has happened in many stories until now.
- Farmer has a cow who is lonely, the farmer gets a new one as a friend. 
  - A very sparse example
  - “kind” word is separately colored. “happy” is again not. In a separate phrase “the kind farmer”, only “farmer” is colored. 
  - This specific story has many instances of things like the phrase “The farmer wanted to help” colored but “help” is not colored. In fact, we don’t see “help” colored many times (it is colored sometimes).
  - The concrete act of kindness is not fully colored.
- Lily helps a man who had dropped his bag in a grocery store. The man next day gives him candies she wanted before. 
  - Here “help” and “happy” are colored. 
  - The first consistent activation comes in the phrase "▁Lily▁felt▁happy▁that▁they▁could▁help"
  - The act of helping is not colored
  - After the man gives her candy, in the phrase "▁Lily▁was▁so▁happy▁and▁she▁couldn't▁believe▁that", "happy" is not colored, while everything else is


## Calm

TODO in the end, Claude has suggested that it is wonk

## Angry

We see instances of characters being hurt instead of angry here.

- Woman is walking in a park, a man says mean things to her. 
  - We see confrontational behavior from both sides here and their nouns/pronouns are colored in those cases too. 
  - The final resolution is fully dark
  - trigger words: "mean", "rude"
- Goat in a hot weather is miserable. 
  - There is 0 anger here. Its more about the goat being sad/frustrated/miserable. Highs at “it”, “miserable”, “shut”, “hotter”.  “the door was shut. The goat was sad and miserable”.
  - trigger words: "miserable", "shut"
- Lily got sandwich but does not like that it does not fit her mouth. 
  - this is again not a story about anger. Its more about frustration.
  - “frustrated”, “burned”, “the sandwich fell apart”. It feels more about being hurt.
- Alligator tries to hunt bunny. it fails. 
  - phrases "The▁alligator▁wanted▁to▁catch▁the▁bunny", "▁The▁alligator▁tried▁to▁catch▁the▁bunny,▁but▁he▁was▁too▁heavy▁and▁slow" are lit up reasonably well. These are phrases of a sort of hunt.  
  - "▁the▁alligator▁was▁still▁hungry" is lit up
  - The initial phrase "▁He▁was▁very▁hungry▁and▁wanted▁to▁eat▁something." was not lit up
- Benny eats something which is yucky. 
  - We again have hurt on a character instead of anger. The sentence "▁Suddenly,▁Benny▁realized▁that▁the▁carrot▁didn't▁taste▁good▁at▁all!▁It▁tasted▁very▁yucky▁and▁made▁his▁tummy▁hurt" is consistently colored 
- (#9) A bug named Buzz steals a bulb from a spider, the spider gets angry and chases him.
  - This one actually has real, directed anger, not just a character being hurt. "▁The▁spider▁was▁angry▁and▁chased▁after▁Buzz" is the peak of the whole story (86.19 on "angry" alone), higher than any peak we've seen in the other angry stories.
  - Unlike the happy/kind stories where "was" consistently beats the trigger word next to it, here "angry" (86.19) beats "was" (28.67) by a wide margin. The literal emotion word dominates for once.
  - The concrete act itself ("chased after Buzz") is lit up too, unlike kind stories where the concrete act of kindness is usually dark.
  - The rest of the story still fits the "something bad happening to a character" pattern: Buzz being scared is dark, the chase getting closer is lit, and it goes dark again once Buzz is safe.

## Sad

- Tims TV stopped working and he got very sad. 
  - trigger words: "sad", "bored"
  - phrase: "▁he▁started▁to▁complain.▁He▁was▁sad▁and▁bored" is colored.
  - In general, we have many sentences colored throughout. The activations feel more "spread out"
- Lily is scared from a nightmare. This is more about “scare” than “sad” though. 
  - trigger words: "scared", "weak"
  - The initial sequence "▁very▁scared▁of▁the▁dark▁and▁had▁a▁nightmare▁every▁night.▁One▁day,▁she▁told▁her▁mom▁about▁her▁nightmare." is one of the bigger consistently colored phrases
  - The scary object itself never fires: "monster" and "closet" stay dark every time they appear (3 occurrences of "closet", all dark), even while the fear-language around them is colored.
  - The comforting resolution is completely dark: once the mom starts reassuring Lily ("don't worry, I'll check your closet"), activation drops off, and the actual resolution line ("let's go play with your toys and forget about that scary nightmare") is fully dark. Same "resolution kills the signal" pattern seen in kind/angry, now confirmed for sad too - matches what we found in the hindi giant story (the happy resolution there was also completely dark).
  - In line with the fact that negative emotions are tracking the emotional state of something bad happening to a character
- Lily lost her doll. 
  - "Lily started to cry and her mom tried to comfort her.” is strongly colored, and the peak of the whole story is on "cry" (62.31), not "sad" (53.34). Same as the hindi Joyce story ("she cried" was the strongest activation there too) - the behavioral verb for an emotion seems to fire more reliably than the static adjective naming it.
  - The penultimate sentence “Lily realized that the noise was too much for her and she felt a little deaf. She decided to leave the factory and go home with her mom” is also colored.
  - "happy" is dark both times it appears in this story, not just at the resolution - even mid-story ("She was so happy!" seeing dolls that look like hers, before the twist) it's 0.
  - The comfort-dialogue is dark again: "Don't worry, we'll find your doll," she said." is fully dark except a stray tokenization fragment. Third story now (TV, nightmare, this one) where a character's spoken reassurance produces nothing even while the narration around distress lights up freely.
  - The middle "doll factory excitement" detour (Lily getting excited, thinking she might have found her doll) is completely dark - good negative evidence the vector isn't firing on "anything emotionally charged", it correctly stays quiet through a stretch of genuine positive excitement sitting in the middle of an otherwise sad story.
- #6. The goat being miserable in hot weather. This is the one from anger. It makes sense for this story to be inside this category.
  - The sad vector is activating with a larger frequency. "sad and miserable" are the peak - "sad" itself is the single highest token in the story (44.0), unlike almost every other case where a copula/connector beats the named emotion word.
  - Diffed directly against angry on the identical text: "The▁goat▁was▁sad▁and▁miserable." -> sad=44.0 on "sad", angry=0.0 on the same token. Angry skips this sentence almost entirely.
  - "The▁sun▁was▁getting▁hotter▁and▁the▁goat▁was▁getting▁thirstier." is angry's territory (5-19), completely dark under sad (0 throughout) - the escalating-discomfort sentence doesn't read as sad.
  - "The▁goat▁tried▁to▁push▁the▁door▁open▁but▁it▁was▁too▁heavy." is angry's peak (29.7 on "it"), sad only picks up the tail ("but it was too heavy.").
  - The ending is the clearest divergence: "The▁goat▁did▁not▁survive▁the▁hot▁day.▁The▁end." stays lit under sad all the way through "The end." (18-32), while angry is almost completely dead here (0 except two weak tokens). Sad is willing to stay engaged through a terminal, unhappy ending; angry needs an active ongoing conflict/obstacle and has nothing left once the goat is just dead.

Overally, sadness also seems to be about “hurting” instead of the normal sad thing I would associate stories with. 

## Desperate

- The goat being miserable in hot weather. This has actually colored quite a lot of tokens in the story. Along with full phrases. This makes sense, this story is really about desperation.
  - The largest frequency compared to "sad" and "angry" vectors for this story. Peak is 68.69, higher than sad's 44.0 and angry's 29.7 on the same text.
  - Strong colors in this whole section: "The▁goat▁looked▁for▁another▁way▁inside▁but▁there▁was▁none.▁The▁sun▁was▁getting▁hotter▁and▁the▁goat▁was▁getting▁thirstier.▁The▁goat▁tried▁to▁push▁the▁door▁open▁but▁it▁was▁too▁heavy.▁  "
  - "The▁goat▁looked▁for▁another▁way▁inside▁but▁there▁was▁none." is entirely unique to desperate - both sad and angry are 0 here. The "tried an alternative, it also failed" beat is desperate's own territory.
  - It is practically a superset of angry activations, colors most of what angry does and more, at higher magnitude.
  - Two places it does NOT subsume the others though: "sad" itself is 0 under desperate (same blind spot as angry - only the sad vector fires on the literal word), and "The▁end." is completely dark under desperate (same as angry) while sad stays lit all the way through it.

- Timmy fell inside a hole. Again, the whole big phrase is colored. Desperation is actually caught quite well. We don’t have individual specific words being caught at all. It catches full sentences which definitely feel desperate to me.
  - "Timmy▁tried▁to▁yell▁for▁help,▁but▁no▁one▁could▁hear▁him.▁He▁started▁to▁get▁scared▁and▁didn't▁know▁what▁to▁do.▁He▁tried▁to▁shrug▁his▁way▁out,▁but▁he▁couldn't.  " is sustained 40-80 throughout, peak is "and" at 80.69 (beats "scared" at 58.2 right next to it, same function-word-over-content-word pattern as everywhere else)
  - triggers: "scared", "yell", "help"
  - The setup ("Timmy loved to play outside, but he never listened to his mom") isn't fully dark like in other categories - mild activation (17-24) on "he/mom/told/him" even before the fall. Desperate seems less strict about requiring a "turn" first.
  - "but▁it▁was▁too▁late" (the tragic outcome, mom finds him too late) stays lit (21-28) - a bad/unresolved outcome keeps the signal going.
  - But the tacked-on moral right after ("Timmy had learned a hard lesson - to always listen to his mom...") dies almost immediately after "Timmy had learned a" - the generic lesson-coda goes dark even though the tragic outcome right before it didn't. Same shape as Tom's "learned to be more careful" ending in kind.
- Timmy the mouse finds a cat nearby and is scared he will be eaten. 
  - Oddly, the "scared" at the end is colored (in the phrase "Timmy was no longer scared") - it survives explicit negation, unusual for an emotion word.
  - Everything else seems reasonably typical of other desperation stories
  - Record peak for the whole session so far: "He▁thought▁about▁running▁away" -> "He"=111.12, and the whole "was so scared that he didn't know what to do... thought about running away, but he knew the cat was faster" stretch sits at 52-111 almost without a dip.
  - Unlike every other story checked, the exposition here is NOT dark: "Timmy was always scared of everything and everyone. He would hide in his little hole all day, every day." is already warm (16-76) from the very first sentence. Likely because this backstory directly states the character's persistent emotional trait, rather than being neutral scene-setting - "exposition is dark" really means "emotionally neutral exposition is dark".
  - Resolution goes dark again ("stood up to the cat. To his surprise, the cat just walked away." - fully 0), and the closing moral ("He learned that sometimes, even the smallest of creatures can have the biggest courage.") dies too, same as the hole story.
- Lily had a nightmare and her mom comforted her
  - Repeats from the sad section. both have quite similar activation patterns.
  - Desperation lights up on scary things like "closet", "nightmare" while sad does not
  - Desperate did not light up on "What
  did you dream about, sweetie?". A calm phrase from her mom. Sad did light up here too
- Alligator is trying to hunt a bunny
  - Repeated from angry story
  - desperate is active for longer runs in the text compared to angry. 
  - "▁and▁was▁scared.▁The▁alligator▁wanted▁to▁catch▁the▁bunny,▁but▁the▁bunny▁was▁too▁fast." -> desperation of the alligator?
  - "The▁bunny▁ran▁away▁from▁the▁alligator▁as▁fast▁as▁he▁could" -> desperation of the bunny?
  - This story does have more flavors of desperation compared to angry

## Disgusting

This is the first emotion with negative values being in the top 90 percentile of the activations.  
Disgusting seems to have the weakest activation patterns from the other emotions.  
We have many stories copied over from sad/angry sections too.
One of the problems might be the small subset of the dataset we are testing this on (we only pick from the top 100 stories).   

- Goat miserable in heat. Story repeated in all bad valence emotions at this point. It also does not make sense that the story is here. I’m not sure why. “miserable” is strongly colored.
  - Diffed against sad/angry/desperate on identical text: disgusted's peak here is 22.0, by far the weakest of the four (sad=44.0, angry=29.7, desperate=68.7). This is consistently the runner-up-or-worse everywhere it fires, no sentence where it's the standout vector - looks like leftover correlation, not real content.
  - First story where genuinely negative values show up: several ordinary narrative words dip slightly negative ("the"=-1.88, "there"=-3.07, "tried"=-3.27, "day"=-4.48). Small and scattered, not a coherent anti-signal, but this is the first time any vector in this session has gone negative on this text.
- A bunny named Benny ate a yucky carrot.
  - "▁It▁tasted▁very▁yucky▁and▁made▁his▁tummy▁hurt" is strongly lit, peak of the story (79.5 on "tasted") - much higher magnitude than the goat story, good confirmation this one genuinely belongs here.
  - This story makes sense here
  - Clean contrast: "yummy" (describing carrots normally, early in the story) is completely dark, while "rot"(40.1), "bad"(13.9), "yucky"(75/62) all fire strongly later - the vector distinguishes the positive taste-word from the negative ones on the same topic.
  - "carrot" itself fires strongly (70.0) - a genuine exception to the pattern where the object of a story stays dark (necklace, toy, doll etc. in other categories) - makes sense since disgust is a property *of* the object (its taste) rather than separable from it.
  - "rot" is actually the first spike in the story, ahead of the bite/reaction - catches the cause of the disgust slightly before the character's reaction to it.
  - Ending ("From that day on, Benny made sure to only eat fresh carrots.") is dark again, with the same small-negative-dip pattern ("sure"=-1.31).
- Lily at a big sandwich and was annoyed since it did not fit her mouth. 
  - Does not make sense for the story to be here.
  - lighting up on "food falling apart" suggests that the model has associated disgust with food problems. 
  - Diffed directly against angry (same text as angry story #3): tracks angry's shape but consistently weaker (peak 44.4 vs 55.0) - except two sharp divergences. "frustrated" itself is angry's peak-ish region (43.7) but weak under disgusted (7.8) - the named emotion stays angry's turf.
  - The burn/pain section goes genuinely negative under disgusted while angry stays positive: "finger"(-3.13), "cried"(-3.07), "pain"(-3.82) vs angry's 10-22 on the same tokens. Real anti-signal on injury/crying content, not just "doesn't care".
  - The one place the two vectors are nearly identical is "but▁it▁just▁fell▁apart." (44/44/42 vs 36/40/42) - the food-texture-failure sentence, which is genuinely disgust-adjacent, unlike the rest of the story.
- Man says mean things to lady. Again does not make sense to be here
  - The patterns are also extremely similar to those of the angry vector on this story. The activations are just smaller in this case.
  - Are all the vectors giving some baselines for valence?
  - Diffed directly against angry: unlike the sandwich story, this one shows no localized divergence or match - disgusted is just angry scaled down ~60-75% almost everywhere ("who"=73%, "man"=61%, opening quote=58%), no sentence where disgusted does anything angry isn't already doing better. This is the cleanest case of pure borrowed correlation with no independent content.
  - Both vectors agree completely on where the story stops mattering - the reconciliation/happy ending is fully dark under both.
- Lily looking at a butterfly. A kid points and says she’s looking at a bug, “bug” is colored strongly. 
  - The phrase "▁He▁was▁pointing▁at▁her▁and▁saying,▁"Look▁at▁Lily,▁she's▁just▁staring▁at▁a▁bug!" is also colored
  - It is not clear why the other parts are colored (it seems to be more about embarrasment). This again might be the fact that disgust is simply activating for bad valence. 
  - Important nuance: "butterfly" itself is dark (0) both times it appears, even in the loving description ("gazed at it, amazed by its beauty"). The vector isn't reacting to "an insect is present" - it's reacting to the *word* "bug" being deployed as a put-down, independent of what's actually being looked at.
  - The embarrassment content ("wanted to run away and hide") fires almost as hard as "bug" itself (29-42) - disgust and shame/embarrassment are known to be psychologically related (both involve a withdrawal/avoidance response), this might be genuine rather than just "bad valence bleed".
  - "not▁be▁ashamed" fires (19.4, 16.6) even though "ashamed" itself stays dark - same negated-word-survives-via-scaffolding pattern seen elsewhere.
- A smelly whale learns to rub himself against a rock to clean himself. This one specifically makes sense here. Its also good that its not present in the other cases. “smelly” is specifically colored a lot.
  - "smelly" (49.3) is genuinely the peak of the story, beating the surrounding copula/connectors - third time now (after carrot, bug) that a literal sensory/physical-property word wins outright, unlike abstract emotion words (happy/sad/kind) which usually lose to "was"/"and" next to them.
  - "smelly" survives negation three separate times in this one story: "a▁way▁to▁not▁be▁smelly" (36.9), "he▁was▁not▁smelly▁anymore" (18.3/15.6), and even "did▁not▁like▁the▁smell" barely dents on "not" while everything around it stays hot. Contrast with "scared"/"ashamed" elsewhere, which mostly do go dark when explicitly negated. Sensory/physical-property words look less sensitive to negation than abstract emotional-state words for this vector.
  - The concrete cleaning act ("rubbed against the rock to clean himself") picks up real signal (9-21), unlike kind stories where the concrete act of kindness is consistently dark - disgust/sensory content cares about the physical act itself.
  - "green" (describing the plants) goes negative both times it appears (-2.55, -2.95) - same small-negative-dip pattern on neutral descriptive words seen in every disgusted story so far.
  - Closing "lived happily ever after" is dark again, same as the farmer story in kind - generic fairy-tale closers reliably die regardless of category.


# Open threads / cross-vector observations (english, session notes)

Loose ends from going through the english reports directly (parsing tokens/values, not just eyeballing) that don't fit cleanly into a single story bullet above. Flagging for later, not yet folded into the sections above.

- **Kind vs happy is not a subset relationship.** Found one story with byte-for-byte identical text across both reports (the "sweet dog Max and Sue find an injured bird" story). The two vectors split cleanly along the story's three acts instead of one nesting inside the other:
  - Act 1 (mutual friendship, "they jogged and played, having a lot of fun") — happy fires, kind is silent (all 0).
  - Act 2 (finding the hurt bird and caring for it, "they had to help the bird... cared for it... after some days") — kind fires hard, happy is silent (all 0).
  - Act 3 (resolution, "were very happy... played together... one more friend") — both fire together, closely matched values.
  - So it's closer to "two overlapping-but-distinct triggers sharing a common happy-ending core" than "kind is a stricter/filtered happy." Would be good to find more exact-text pairs across reports to confirm this holds generally (only one pair found so far via exact string match).
- **Self vs other, kind vs happy.** In the Sue/candle story, the receiver (mom) gets the literal word "happy" ("her mom was so happy") and it's one of the hottest spans in the story; the doer (Sue) never gets "happy" at all — she gets "proud" instead ("Sue felt proud that she could help her mom"), and that fires too. So "happy" attached to the self doesn't fire under the kind vector, but "happy" attached to the other person does. Matches the same pattern already noted for the hindi flower story (receiver's happiness lighting up more than expected).
- **Angry looks like the mirror image of kind: "bad thing being actively done to a character" vs "good thing being actively done for a character."** Across the angry stories checked (park/rude man, goat, sandwich/burn, bug/spider), the vector consistently fires while harm/thwarting is actively happening to a character and goes dark the moment it resolves (apology accepted, comfort given, danger passed) — it doesn't linger on the aftermath or on how anyone feels in retrospect. This is the same shape as the hindi finding (angry ≈ "something happens to a character that they don't want"), now confirmed the same way in english.
- **The concrete act itself being dark seems specific to positive/kind acts, not universal.** Kind acts described in a single quick clause (lighting a candle, tearing off a piece of steel, getting a companion cow) are consistently dark; only acts drawn out over multiple sentences with a time-passage beat light up (the bird story). But in the angry bug/spider story, the concrete angry act ("chased after Buzz") is lit up immediately, no dwelling required. So "acts are dark" is not a general rule — it may be more that expressing genuine first-person emotion (proud, angry) fires directly, while depicting an altruistic action performed by someone else needs to be lingered on before it registers.
- **"Was"/copula beating the trigger word next to it (was > happy, was > kind) does not hold for angry.** In the bug/spider story "angry" (86.19) beats "was" (28.67) by a wide margin — the only case seen so far where the literal emotion word wins outright over its scaffolding.
- **Ending-sentence-is-the-peak looks happy/excited-specific, not universal.** Reliable across ~5 happy stories, but broke down repeatedly in kind (farmer's "happily ever after" is dark) and angry (multiple stories fizzle out with no ending spike, since resolution kills the signal there).
- **"loved"/"love" being dead is not universal either** — reliably dead under happy/excited, but fired under kind ("Tom... loved to help people").
- General methodology note: manual index-counting from the raw token/value arrays is unreliable for anything beyond a quick sanity check (caught one real misalignment this session, on the Freddy "jumped up and down with excitement" clause) — always verify with an actual parse before asserting a specific token's value.

# Hypotheses to test

- If a character name is broken up, the model colors the later parts more than the earlier parts. Needs statistical analysis.
- Kind vector is firing on a subset of happy vector firings i think. It is useful to first check this statistically and then analyse the neural activity.
- Desperate fires for a lot of places where angry does too. Check if angry is a sort of subset of desperate? Can we find the neurons which are different between them and see their reports?
- Hindi tokenisation cuts up a lot of words. Many times, when a specific emotion is running and it ends with a negative (he kept fighting and fighting and “won”) (a climax different from what is happening until now), the keeps coloring until the negative word. In hindi this word can be cut up, the model colors up the first parts of that word and stops coloring the last part (does it realise the word’s full meaning at that point?).
- Disgusted basically has the same stories and activation patterns as angry. The peaks are different though. This is a small enough difference that is worth checking out.
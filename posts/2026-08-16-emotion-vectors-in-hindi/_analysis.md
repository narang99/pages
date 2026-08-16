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

# Hindi activating stories

Hindi stories in general are harder to parse for two reasons:

- Tokenization is cutting up words
    - Due to this, for token level statistics, it would be useful to specially handle this.
- The Hindi translation itself is slightly bad, and the sentences read very complicated
    - The translation quality is also not perfect, but not bad at all.

Most of the nouns (character names) are cut by the tokenization, but the LLM in the end generally ends up coloring the last letter of these names (has it figured it out by then and using that as a marker?)

I feel there is a general overuse of the literal translations of “happy” in the hindi stories being caught. I’m not sure if subtle emotions are captured by the model. If the terms are present in the sentence, the sentence is colored to a large extent.

## Happy

- A girl likes nature. Plays around. Is having fun. We consistently see pronouns like “वह” (they) being colored. “मुस्कुराई” (smile) is fully tokenized into individual letters but is nevertheless fully colored. Same for “खुशी” (happiness). Large portions of sentences where the girl is feeling good are colored too.
- A joker comes to visit Sammy and he is very happy. We again see the problems of tokenization. The noun “सैमी” (Sammy) was split at one place and a portion was not highlighted. “उत्सव” (a synonym for happiness) was also split and a small portion was not highlighted. Otherwise the overall characteristics are similar. Large portions of happy sentences are colored.
- Timmy goes to friend’s party. Gets goodies. His gift contained a truck and he was very happy. “हँसे” is partially colored but was cut during tokenization. When a noun like “टिम्मी” (timmy) is colored, it is colored by the end (only the last letter is colored). Is the LLM understanding what the word means by the end and is coloring only that part? Full sentences ”जल्द ही सभी को एक साथ बहुत मज़ा आ रहा था” (soon everyone was having fun together) are colored too.
- Amy’s mother forgot to turn off the stove. Amy does it. They laugh about the incident. Tokenized broken words “हंस” (laugh) and “हंसमुख” (a cheerful person) are fully colored (not partially). Similar to other stories.

## Excited

- A joker comes to visit Sammy and he is very happy. Story repeated from happy. More words are colored though. Apart from the words which were colored in happy, we have more words colored here. “आश्चर्य” (wonder/surprise). The only difference I feel is that the first sentence is more colored. Not sure if there is any hard evidence here.
- Tommy sees a mound of candy in park and is excited. “उत्साहित” (excited) is consistently colored (cut up though). “वह अपनी आँखों पर विश्वास नहीं कर सकता था” (he couldn’t believe his own eyes)
- Timmy goes to friend’s party. Gets goodies. His gift contained a truck and he was very happy. Overlap with the happy story
- Two kids opened a very old wardrobe. A sudden magical chest started walking towards them and the wardrobe started turning new. “रोमांचक” (thrilling) is colored. “ उन्होंने विस्मय में चारों ओर देखा और जादू के गायब होने से पहले जल्दी से छाती को बंद कर दिया।” is the sentence with the most continuous color.
- Lily’s dresser turns into a magical carriage, she wears a pretty dress and drives the carraige around. This was a very hard story to read, the translation seems off

# Kind

- A kind bear helps a friend. “समर्थन” (loosely translates to helping here) comes but is not colored weirdly. I don’t see a trigger word of sorts (nothing obvious at least). The whole vibe of the story is that of helping so it makes sense. We see consistent colors coming up in this.
    - Full setences partially colored: “वह हर दिन अपने दोस्त का समर्थन करता रहता था और जल्द ही उसके दोस्त ने दुखी होना बंद कर दिया।” (Everyday he kept helping his friend and soon the first was no longer sad) (”was no longer sad” is not colored)
- A girl rides the bus with her mom and everyone makes sweet funny faces to light her up, she likes it. One day she makes a paper flower for her mother
    - This story has some feeling of being similar to happy stories, but it also does have the overall topic of the main character making someone else happy.
    - I suspect we would have happy and kind vectors lighting up together in some text for different characters. Would be useful to see how they interact.
    - Words: “मुस्कुराए”,
    - “ लड़की अपने मम्मी के लिए कुछ खास बनाना चाहती थी” is partially lit up (Girl wanted to make something special for her mothing).
    - “ उसने अपने मम्मी को फूल दिया। उसकी मम्मी बहुत खुश थी और उसने उसे एक बड़ा गले दिया” (she gave her mother the flower. her mother felt very happy and hugged her). We have strong activations on the part where the mother is happy (we would expect happy vector to go high on that, this is different and slightly unexpected)
    - We have this happening multiple times. The receiver of kindness is also lit up.
- A bird loves helping others in the village.
    - “दयालु” (kind), “देखभाल” (taking care), “मदद” (help), “सावधानी” (attentive)
- A girl loves nature and is playing in it. Repeated happy story. Interestingly the activation patterns are quite different for the kind vector
    - The phrase “वह बहुत खुश थी” (she was very happy) has 0 color in kind stories, while the happy counterpart has it fully colored.
    - The phrase “प्रकृति लड़की को देखकर मुस्कुराई” is partially colored (possible because tokenization is breaking the words, each word is partially colored at least). Happy also has it colored. It seems kindness vector might be a more stricter happy vector? This needs confirmation.

# Angry

- A bug is a disease-carrying pest. A bird hunts the bug. No obvious hints of anger. The story simply keeps a sort of negative vibe of spreading germs (hurting others). “कीटाणुओं” (germs) is consistently colored. “ जबकि बुरा बग कीटाणुओं को फैला रहा था” (The bad bug was spreading germs) is colored. Similar “ पक्षी झपट्टा मार दिया, और एक झपट्टा मारने के साथ, बग जमीन से दूर था” (The bird snatched its prey and the bug started getting farther from land). This phrase is also fully colored. Both are cases of hurtful activity.
    - Words to track later: “कीटाणुओं”, “झपट्टा”, “मारने”, “फैला”, “बुरा”, “गंदे”
- A girl’s table was dirty, she tried cleaning it but couldn’t. This is also not about anger but about frustration or sadness. Interestingly the initial “परेशान” (concerned) is not colored even though it is a strong word. The second occurence is colored (in the sentence “ मेज पर गड़बड़ रही। लड़की बहुत परेशान थी” [there was trouble on the table. The girl was very concerned], the whole sentence is however, colored]. The middle part of the story involves the girl going out looking for soap ( उसने साबुन खरीदा और फिर वह टेबल धोने के लिए घर चली गई। उसने साबुन को मेज पर रखा और उसे रगड़ना शुरू कर दिया।). This part is not colored. Weirdly the last occurence of “दुखी” (sad) is not colored
    - Words to track: “परेशान”, “गड़बड़ी”, “दुखी”
- A hero likes his rocking chair but breaks it. He couldnt fix it: This is the first story which contains an angry instance “ वह चिल्लाया और दीवार पर मुक्का मारा, लेकिन यह मदद नहीं की” (He screamed and punched the wall but it did not help). This phrase is also strongly colored compared to others. The other parts are about sadness in not being able to fix his chair. The top projection values are quite high (compared to other values like kind also).
    - words to track: “चिल्लाया”, “मुक्का”, “दोषी”, “दुखी”, ”निराश”
- A boy explores a dead wheat field and is bitten by some animal, he gets angry and catches it.
    - The word “गुस्से” (angry) comes up. Its one of the highest activations in the report.
    - This story has the arc of “the main character gets angry on being bitten → plans on how to catch the animal → actual hunt phase”. The angry phase is colored strongly. The strategic thinking phase of planning the hunt is fully dark (no coloring). Actual hunt phase is colored similar to the first bug+bird story.
    - words: “धोखा”, “गुस्से”
- Millie is a 1 year old child who has a habit of eating random things. Her mom keeps lecturing her not to.
    - “ उसने जो कर रही थी उसे रोक दिया और मिल्ली ने उन चीजों को चबाने के बारे में एक बड़ा व्याख्यान दिया जो भोजन नहीं थे।” → The mom stopped millie from eating random things and gave her a long lecture on the fact that she should only chew edible stuff. This is a much gentler instance of something happening to a character which they don’t like (in the first story it was hunting, in this it was lecturing). This is in exact opposite contrast to kind where something good was happening to a character.
        - We will need to see if “angry” and “kind” are directionally opposite?
    - There are no angry instances here though.
    - The ranges are making sense now though. Exact angry instances have large spikes on this vector (we saw that in some of the previous stories). Angry vector has consistent projections on actions being done to a character that they don’t want. Our extraction method sorts stories by picking stories with highest count of activations > 90 percentile of all the activations. In this case, it simply might be that angry sentences are short and spiky in the dataset.

## Sad

- a mother and daughter look up at the stars everyday. One night the stars are different. The mother feels something bad is coming. They wake up to the city destroyed by a tornado.
    - A large number of words are colored in this text. Even the setup where the story talks about how the mother talks to the daughter about stars everyday is colored.
    - Interestingly “उसकी बेटी ने पूछा, "मम्मी, सितारे एक ही क्यों नहीं हैं?” (The daughter asked, “mom why are the stars not the same?”) is colored stronger than “ लेकिन माँ को पता था कि कुछ बुरा होने वाला है” (The mom knew something bad was going to happen). “बुरा” (bad) is weaker than the others.
    - The strongest spike is at the literal word “दुखी” (sad).
    - trigger words: दुखी, डर
- A hero likes his rocking chair but breaks it. He couldnt fix it: Repeated from the angry instance. We see different activation patterns though.
    - The phrase “ वह चिल्लाया और दीवार पर मुक्का मारा” (He screamed and punched the wall) has pretty much 0 colors (no high activating tokens). For the angry vector, this was the largest activation. This is the first instance of seeing the difference between angry and sad side-by-side.
    - Phrase “ वह खुद में बहुत दुखी और निराश था” (he was very sad) is lit up . The last closing sentence is fully colored ( उन्होंने महसूस किया कि वह कुर्सी को कभी ठीक नहीं कर सकते, इसलिए उन्होंने अपना सिर लटका दिया और चले गए। उनकी बुरी गलती ने उन्हें बहुत दुखी कर दिया था और कुर्सी हमेशा के लिए चली गई थी।) (He realised that he can’t fix the chair. He walked away with a hung head. His mistake made him very sad and the chair was gone forever).
    - trigger words: दुखी, निराश, दोष
- Joyce loves dressing up. A pin in her dresses pricks her finger. She had to go to the doctor to get it out
    - Much weaker emotion than the other stories. Weirdly “ वह बहुत खुश” (she was very happy) is partially highlighted (the word “happy” is split and the first part is highlighted, while the second is not, maybe the model figured out the meaning by the end which conflicted with the emotion vector?)
    - “वह अपने दोस्तों को रोया ” (She cried with her friends) has the strongest activation
    - “ जॉयस को इसे हटाने के लिए डॉक्टर के पास जाना पड़ा।” (She had to go to see the doctor) is also colored consistently. (The last sad/feeling  part?)
- John sees a giant walking alone outside. He picks flowers for the giant.
    - The story has a warm ending. It starts with John seeing a giant who looks lonely. The main thing the projection is firing on is the lonely part for the giant. The story takes a happy turn in the end where John meets the giant and takes him to his home. The happy resolution part is completely dark.
    - Phrases firing up: “ अकेले चलते हुए” (walking alone), “लेकिन यह बहुत अकेला दिखता है।” (but he looks very lonely).
    - There are some other interesting parts of the story:
        - “ कि यह विशालकाय से” (meeting the giant) “ लेकिन वह केवल तीन” (but he was only 3 years old). are colored (they are part of the same phrase “he thought meeting the giant would be fun but since he was only 3 years old he had to ask his mother)
            - I can speculate that it is coloring parts where the character wants to do something but can’t do it directly, or there are obstacles to it
    - trigger words: “अकेला”, “अलविदा”

# Desperate

- A hero breaks his rocking chair. He gets angry. He tries to fix it but he can’t.
    - This is a repeat from sad and angry sections. We see a larger number of words being colored though.
    - The difference is generally where the peaks of the vector’s alignment come.
    - Unlike the section in sad where the phrase “ वह चिल्लाया और दीवार पर मुक्का मारा” (he screamed and punched at the wall) was completely dark, we have pretty good coloring in this section
    - The peaks happen at “ उसने कुछ ऐसा किया था जिसे वह पूर्ववत नहीं कर सकता था। नायक को बहुत दोषी लगा।” (he had done something which couldn’t be fixed. He felt very guilty). This makes sense. This is in line with desperation where a situation cannot be changed.
- A boy idolises a hero. The hero is in danger. The boy tries to help the hero. The boy succeeds.
    - This is a repeat from angry section. Reasonably different patterns
    - First thing is we see a repeat of desperate coloring a lot more than what angry does (80% of what angry colored is colored by desperate, vice-versa is not true)
    - In this story, angry lights up strongly on the villain’s harmful act. It also lights up strongly on the final fight.
        - Desperate however, also lights up on phrases like “ उनका नायक बहुत खतरे में था!छोटा लड़का बहुत डर गया था।” (his hero was in danger and the boy was scared), “किसी तरह अपने नायक की मदद करने की कोशिश करनी थी।” (somehow help his hero), “ वह इतना असहाय महसूस कर रहा था!” (he felt helpless),
        - It lights up weakly in the phrases where angry does
    - trigger words: असहाय
- A girl’s table was dirty, she tried cleaning it but couldn’t.
    - A repeat from the angry section
    - Again, desperate is lighting up more than angry
    - Angry was lighting up a situation a charater does not like. Desperate does too.
    - Additionally, desperate peaks around the parts where the character is trying hard to clean it. “ उसने कोशिश की और उसने कोशिश की लेकिन यह बंद नहीं होगा।” (she tried and tried but she couldnt fix it). Note that this also lit up in the angry. It’s just that the peaks are different.
- A frog loves jumping. He wants to jump so high that his feet touch his house’s top. He succeeds. He soon realises he is in danger since going down would be risky. He realises he has no choice but to risk it and jump.
    - This feels like a very good example for desperation. The main phras” यह वापस कूदने के लिए बहुत दूर था।मेंढक जानता था कि वह फंस गया है और वह डर गया था। उसने मदद मांगी लेकिन किसी भी जानवर ने उसे नहीं सुना। निपट अकेले पड़ गये वह। कुछ समय बाद, मेंढक को पता था कि उसे जोखिम उठाना होगा। किसी तरह, वह घर से कूदने में कामयाब रहा” (Jumping back was very far. He knew he was trapped and got scared. He asked for help but nobody heard him. After a while, he knew he had to take the risk. Somehow, he was successful in jumping back) is consistently colored.
        - Interestingly a partial part of “कामयाब” (successful) is colored (the first part)
        - This pattern was repeated. A negative word for the emotion is partially colored in the beginning while the emotion train is running. Once the word finishes (the model finally understands the meaning of this word? the coloring stops)
    - trigger words: फंस, डर, जोखिम
- A boy finds a bug in his pocket while out walking — a bad surprise! He's scared and desperately wants to get rid of it, so he screams and runs, dashing home and rushing inside. His mom hears his screaming and asks what happened; he explains about the bug in his
pocket. She calmly tells him not to worry and takes the bug outside. Relieved and happy to be rid of it, he vows to never let that happen again, and from then on checks his pockets extra carefully.
    - The story repeats from angry section. It seems all bad valence emotions fire on stuff where “something happens to the character that they don’t want)
    - Desperate again is firing for more tokens than angry did
    - Extra phrases like “ और जल्दी से अंदर भाग गया” (and he ran inside) are colored in desperate.
    - It seems desperate does color most of what angry does, it is less selective. It would be useful to analyse which neurons are different between them and see what they are firing on specifically.

# Disgusting

- A bug is a disease-carrying pest. A bird hunts the bug. No obvious hints of anger. The story simply keeps a sort of negative vibe of spreading germs (hurting others).
    - Repeat from angry section. There is a large intersection in the tokens they have colored.
    - The only difference is that the disgusted version is only peaking at the initial sentence “ एक फिल्टी बग था जो हर किसी के लिए कीटाणुओं” (one bug who spread germs). The activations afterwards are present but much weaker. Angry had stronger activations on the hunting part.
- A girl’s table was dirty, she tried cleaning it but couldn’t.
    - Again, very similar to angry section. Overall both of them color similar things
    - Peaks are different. “गंदगी” (dirt) is the peak for disgust. For angry it was “ लड़की बहुत परेशान थी” (she was very annoyed)
- A boy explores a dead wheat field and is bitten by some animal, he gets angry and catches it.
    - Again copied from angry
    - Peaks are also quite similar here. The activation pattern is quite similar. Angry has another extra peak at “गुस्से” (anger)
- A hero breaks his favorite chair while rocking too hard.
    - Copied from angry
    - No difference. It is approximately tracking whatever angry is doing here.

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
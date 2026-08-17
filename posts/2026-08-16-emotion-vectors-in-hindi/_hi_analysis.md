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
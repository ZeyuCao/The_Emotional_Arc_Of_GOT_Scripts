```python
#import 
import pandas as pd
import re
import os
```


```python
#check the working directory
os.getcwd()
```




    'C:\\Users\\Administrator'




```python
#change the working directory
os.chdir('E:\\下载\\project\\GOT\\script\\S1')
```


```python
#reconfirm
os.getcwd()
```




    'E:\\下载\\project\\GOT\\script\\S1'




```python
#webdata scraping

#import
import requests
from bs4 import BeautifulSoup

#get url
url = "https://genius.com/1639510"

#getting response object
res=requests.get(url)
 
#Initialize the object with the document
soup = BeautifulSoup(res.content, "html.parser")
 
#Get the whole page
page = soup.html
 
#Print each string recursively
for string in page.strings:
    print(string)
```

    Winter is Coming - Game of Thrones 
    Lyrics
    About
    Comments
    Sign Up
    Search lyrics & more
    Cover art for Winter is Coming by Game of Thrones
    Winter is Coming
    Game of Thrones
    Track 1 on 
    Season 1 Scripts 
    The first episode of the Game of Thrones series starts, typically, in the icy cold beyond the wall. Things don’t get any warmer as we meet the show’s characters for the… Read More 
    Produced by
    
    D.B. Weiss & David Benioff
    Release Date
    
    April 17, 2011
    View All Credits 
    1
    91.9K
    
    35
    
    10
    Winter is Coming Lyrics
    EPISODE 1 - WINTER IS COMING
    [begining]
    [First scene opens with three Rangers riding through a tunnel, leaving the Wall, and going into the woods. (Eerie music in background) One Ranger splits off and finds a campsite full of mutilated bodies, including a child hanging from a tree branch. A birds-eye view shows the bodies arranged in a shield-like pattern. The Ranger rides back to the other two.]
    
    WAYMAR ROYCE: What d’you expect? They’re savages. One lot steals a goat from another lot and before you know it, they’re ripping each other to pieces.
    
    WILL: I’ve never seen wildlings do a thing like this. I’ve never seen a thing like this, not ever in my life.
    
    WAYMAR ROYCE: How close did you get?
    
    WILL: Close as any man would.
    
    GARED: We should head back to the wall.
    ROYCE: Do the dead frighten you?
    
    GARED: Our orders were to track the wildlings. We tracked them. They won’t trouble us no more.
    
    ROYCE: You don’t think he’ll ask us how they died? Get back on your horse.
    
    [GARED grumbles.]
    
    WILL: Whatever did it to them could do it to us. They even killed the children.
    
    ROYCE: It’s a good thing we’re not children. You want to run away south, run away. Of course, they will behead you as a deserter … If I don’t catch you first. Get back on your horse. I won’t say it again.
    
    [WILL glares, but obeys. Sometime later, the three Rangers return to the campsite, which is now completely cleared.]
    
    ROYCE: Your dead men seem to have moved camp.
    
    WILL: They were here.
    
    GARED: See where they went.
    
    [The three look around, swords drawn. They hear the wind and eerie calls. GARED finds a red cloth in the snow.]
    
    ROYCE: What is it?
    
    GARED: It’s …
    [As he speaks, a CREATURE with glowing blue eyes rises behind ROYCE. ROYCE turns, the CREATURE strikes. The scene shifts to WILL, who hears a man crying out. The three horses stampede past him. He turns and sees someone standing very still in the distance. The figure turns – it’s the child who had been suspended in the tree, now with glowing blue eyes. WILL turns and runs.
    GARED is also fleeing, and we hear strange growls and catch glimpses of the CREATURE. Both terrified RANGERS stop, some distance apart, to catch their breath. WILL sees a CREATURE behead GARED. WILL sinks to his knees and the CREATURE tosses GARED’S head to him.]
    
    [Blackout]
    
    TITLE SEQUENCE
    [Riders from Winterfell come up behind a dazed WILL. The scene shifts to the castle, where BRAN is practicing archery and getting frustrated, under the eyes of JON SNOW and ROBB STARK. JON pats BRAN’S shoulder.]
    
    JON: Go on. Father’s watching.
    
    [We see NED and CATELYN STARK watching from above.]
    
    JON: And your mother.
    
    [Scene shifts to needlework practice with the girls inside the castle.]
    
    SEPTA MORDANE (to SANSA): Fine work, as always. Well done.
    
    SANSA: Thank you.
    
    SEPTA MORDANE: I love the detail that you’ve managed to get in this corners. … Quite beautiful … the stitching …
    
    [As she murmurs to SANSA about the embroidery, ARYA struggles with her needlework and listens to the arrows hitting and the male laughter outside.]
    [Outside, BRAN tries and misses again. Everyone laughs.]
    
    NED: And which one of you was a marksman at ten? Keep practicing, Bran. Go on.
    
    JON: Don’t think too much, Bran.
    ROBB: Relax your bow arm.
    
    [BRAN pulls the arrow back. An arrow hits the bullseye. BRAN (still with his arrow), JON, and ROBB turn in surprise to see ARYA, who curtsies after her perfect shot. ROBB and JON laugh as Bran takes out after ARYA.]
    
    JON/ROBB: Quick, Bran, faster!
    
    [RODRICK CASSEL and THEON GREYJOY approach NED and CATELYN on the balcony.]
    
    CASSEL: Lord Stark. My lady. A guardsman just rode in from the hills. They’ve captured a deserter from the Night’s Watch.
    
    [NED grimaces.]
    
    NED: Get the lads to saddle their horses.
    
    [THEON departs.]
    
    CATELYN: Do you have to?
    
    NED: He swore an oath, Cat.
    
    CASSEL: The law is law, my lady.
    
    NED: Tell Bran he’s coming, too.
    
    [CASSEL nods and departs.]
    
    CATELYN: Ned. Ten is too young to see such things.
    
    NED: He won’t be a boy forever. And winter is coming.
    
    [NED departs. In the courtyard, ROBB and JON gather the arrows. CATELYN turns and glares down on JON. He looks at her and walks away.]
    
    ROBB: Lad, go run back and get the rest.
    
    [Scene shifts, and we see WILL being taken to the block.]
    
    WILL (muttering): White Walkers. I saw the White Walkers. White Walkers. The White Walkers, I saw them.
    
    [He and NED face each other.]
    
    WILL: I know I broke my oath. And I know I’m a deserter. I should have gone back to the Wall and warned them. But I saw what I saw. I saw the White Walkers. People need to know. If you can get word to my family, tell them I’m no coward. Tell them I’m sorry.
    
    NED nods yes, and WILL is positioned on the tree limb that serves as a block. [NED draws Ice from a scabbard held by Theon.]
    
    WILL (whispering): Forgive me, lord.
    
    [NED bows his head over ICE.]
    
    NED: In the name of Robert of the House Baratheon, first of his name …
    
    JON (to BRAN): Don’t look away.
    
    NED: King of the Andals and the First Men …
    
    JON: Father will know if you do.
    
    NED: Lord of the Seven Kingdoms and protector of the realm, I, Eddard of the House Stark, Lord of Winterfell and Warden of the North, sentence you to die.
    
    [NED swings ICE and beheads WILL. BRAN does not look away.]
    
    JON: You did well.
    
    [He walks away. ROBB turns and puts his arm around BRAN and they go to their horses together. NED approaches BRAN.]
    
    NED: You understand why I did it?
    
    BRAN: Jon said he was a deserter.
    
    NED: But do you understand why I had to kill him?
    
    BRAN: Our way is the old way?
    
    NED: The man who passes the sentence should swing the sword.
    
    BRAN: Is it true he saw the White Walkers?
    
    NED: The White Walkers have been gone for thousands of years.
    
    BRAN: So he was lying?
    
    NED: A madman sees what he sees.
    
    [Scene shifts to a dead stag’s head. The Winterfell men gather on the bridge They see a ravaged deer before them.]
    
    JON: What is it?
    
    THEON: Mountain lion?
    
    NED: There are no mountain lions in these woods.
    
    [With swords out, they begin to search. NED finds a dead direwolf with antlers through her throat. Her pups are whimpering around her.]
    
    THEON: It’s a freak.
    
    NED: It’s a direwolf.
    
    [NED and CASSEL glance at each other.]
    
    NED: Tough old beast.
    
    [He pulls out the antlers.]
    
    ROBB: There are no direwolves south of the Wall.
    
    JON: Now there are five.
    
    [Jon picks up a pup and offers it to BRAN.]
    
    JON: You want to hold it?
    
    BRAN: Where will they go? Their mother’s dead.
    
    CASSEL: They don’t belong down here.
    
    NED: Better a quick death. They won’t last without their mother.
    
    THEON: Right. Give it here.
    
    BRAN: NO!
    
    ROBB (disgustedly to THEON): Put away your blade.
    
    THEON: I take orders from your father, not you.
    
    BRAN: Please, father!
    
    NED: I’m sorry, Bran.
    
    JON: Lord Stark? There are five pups. One for each of the Stark children. The direwolf is the sigil of your House. They were meant to have them.
    
    [Everyone looks at NED, BRAN with great hope.]
    
    NED: You will train them yourselves. You will feed them yourselves. And if they die, you will bury them yourselves.
    
    [BRAN cradles his pup as JON hands more pups to ROBB.]
    
    BRAN (to JON): What about you?
    
    JON: I’m not a Stark. Get on.
    
    [JON walks away, pauses, and hears another whimper.]
    
    ROBB: What is it?
    
    [JON pulls up a white wolf pup.]
    
    THEON: The runt of the litter. That one’s yours, Snow.
    
    [Scene shifts to bells ringing at Kings Landing. In front of the Iron Throne, surrounded by druidical looking celebrants, lies the body of JON ARRYN. Up in the balcony, CERSEI watches the scene below as JAIME approaches.]
    
    JAIME: As your brother, I feel it’s my duty to warn you: You worry too much. It’s starting to show.
    
    CERSEI: And you never worry about anything. When we were seven, you jumped off the cliffs as Casterly Rock. One hundred foot drop into the water. And you were never afraid.
    
    JAIME: There was nothing to be afraid of until you told father. [In a whisper, mimicking] We’re Lannisters. Lannisters don’t act like fools.
    
    CERSEI: What if Jon Arryn told someone?
    
    JAIME: But who would he tell?
    
    CERSEI: My husband.
    
    JAIME: If he told the king, both our heads would be skewered on the city gates by now. Whatever Jon Arryn knew or didn’t know, it died with him. And Robert will choose a new Hand of the king, someone to do his job while he’s off fucking boars and hunting whores. Or is it the other way around? And life will go on.
    
    CERSEI: You should be the Hand of the king.
    
    JAIME: That’s an honor I can do without. Their days are too long, their lives are too short.
    
    [Scene shifts to a raven approaching Winterfell. CATELYN crosses a busy courtyard and finds NED in the godswood.]
    
    CATELYN: All these years and I still feel like an outsider when I come here.
    
    NED: You have five northern children. You’re not an outsider.
    
    CATELYN: I wonder if the old gods agree.
    
    NED: It’s your gods with all the rules.
    
    CATELYN: I am so sorry, my love.
    
    NED: Tell me.
    
    CATELYN: There was a raven from Kings Landing. Jon Arryn is dead. A fever took him. I know he was like a father to you.
    
    NED: Your sister. The boy …
    
    CATELYN: They both have their health. Gods be good. [pause] The raven brought more news. The king rides for Winterfell. With the queen and all the rest of them.
    
    NED: He’s coming this far North, there’s only one thing he’s after.
    
    CATELYN: You can always say no, Ned.
    
    [Scene shifts to the Winterfell great hall where a great banquet is being prepared.]
    
    CATELYN: We need plenty of candles for Lord Tyrion’s chamber. I’m told he reads all night.
    
    MAESTER LUWIN: I’m told he drinks all night.
    
    CATELYN: How much could he possibly drink? A man of his … stature.
    
    LUWIN: We’ve brought up eight barrels of ale from the cellar. Perhaps we’ll find out.
    
    CATELYN: In any case, candles.
    
    [Scene shifts to Robb, Theon, and Jon getting barbered.]
    
    JON: Why’s your mother so dead-set on us getting pretty for the king?
    
    THEON: It’s for the queen, I bet. I hear she’s [sleek as a mink?]
    
    ROBB: I hear the prince is a right royal prick.
    
    THEON: Think of all those southern girls he gets to stab with his right royal prick.
    
    ROBB: Go on, Tommy, shave him good. He’s never met a girl he likes better than his own hair.
    
    [Scene shifts to the royal procession approaching Winterfell. Bran sees them from his perch high atop a castle wall and clambers nimbly down to tell everyone. CATELYN and LUWIN walk to the courtyard, passing BRAN’s wolf pup.]
    
    CATELYN: Gods, but they grow fast. [Seeing BRAN on the wall] Brandon!
    
    BRAN: I saw the king! He’s got hundreds of people!
    
    CATELYN: How many times have I told you: No climbing!
    
    BRAN: But he’s coming right now! Down our road!
    
    CATELYN: I want you to promise me: No more climbing.
    
    BRAN (looking down): I promise.
    
    CATELYN: D’you know what?
    
    BRAN: What?
    
    CATELYN: You always look at your feet before you lie. Run and find your father. Tell him the king is close.
    
    [BRAN runs off, followed by his wolf pup.]
    
    [Scene shifts to grand entry of the king’s horses and men. ARYA, wearing a helm and cloak, pushes her way into a tall wagon for a better look. In rides JOFFREY, followed by the HOUND. The other Starks wait in a greeting line.]
    
    CATELYN: Where’s Arya? Sansa, where’s your sister?
    
    [More riders with banners. ARYA scoots past her parents to get in the receiving line.]
    
    NED: Hey,, hey, hey, hey. What are you doing with that on? [Pulls off ARYA’s helm]
    
    ARYA (pushing BRAN): Move!
    
    [JOFFREY rides up, SANSA smiles at him, ROBB glares at JOFFREY. The HOUND pulls up his helm. The coach carrying CERSEI lumbers in, followed by KING ROBERT. All kneel. ROBERT heaves himself off his horse. NED looks shocked at the sight of his old friend, now fat and red-faced. ROBERT signals for all to rise and looks at NED.]
    
    NED: Your Grace.
    
    ROBERT: You’ve got fat.
    
    [NED gives ROBERT a “What about you?” look. They start laughing.]
    
    ROBERT: Cat!
    
    CATELYN: Your Grace.
    
    ROBERT: Nine years. Why haven’t I seen you? Where the hell have you been?
    
    NED: Guarding the North for you, Your Grace. Winterfell is yours.
    
    [CERSEI and her other children descend from the coach.]
    
    ARYA: Where’s the Imp?
    
    SANSA: Will you shut up?
    
    ROBERT: Who have we here? You must be Robb. (To Sansa) My, you’re a pretty one. (To Arya) Your name is?
    
    ARYA: Arya.
    
    ROBERT (to BRAN) Ooh. Show us your muscles. You’ll be a soldier.
    
    [JAIME removes his helm.]
    
    ARYA: That’s Jaime Lannister. The queen’s twin brother.
    
    SANSA: Would you please shut up.
    
    [CERSEI approaches.]
    
    NED: My queen.
    
    CATELYN: My queen.
    
    ROBERT: Take me to your crypt. I want to pay my respects.
    
    CERSEI: We’ve been riding for a month, my love. Surely the dead can wait.
    
    ROBERT: Ned.
    
    ARYA: Where’s the Imp?
    
    [CERSEI, humiliated in front of all, walks back to JAIME.]
    
    CERSEI: Where is our brother? Go find the little beast.
    
    [Scene changes to the crypt.]
    
    NED: Tell me about Jon Arryn.
    
    ROBERT: One minute he was fine, and then … Burned right through him, whatever it was. I loved that man.
    
    NED: We both did.
    
    ROBERT: He never had to teach you much, but me … You remember me at 16? All I wanted to do was crack skulls and fuck girls. He showed me what was what.
    
    NED: Aye.
    
    ROBERT: Don’t look at me like that. Not his fault I didn’t listen. (They laugh. ROBERT sighs.) I need you, Ned. Down at Kings Landing. Not up here, where you’re no damn use to anybody. Lord Eddard Stark, I would name you the Hand of the king.
    
    [NED kneels.]
    
    NED: I’m not worthy of the honor.
    
    ROBERT: I’m not trying to honor you. I’m trying to get you to run my kingdom while I eat, drink, and whore my way to an early grave. Damn it, Ned, stand up. You helped me win the Iron Throne, now help me keep the damn thing. We were meant to rule together. If your sister had lived, we would have been bound by blood. Well, it’s not too late. I have a son, you have a daughter. We’ll join our Houses.
    
    [Scene changes to JAIME in the Winterfell settlement. We see Tyrion inside a whorehouse, swilling liquor and laughing as a woman pops into view after servicing him.]
    
    TYRION: Mmh. It is true what they say about the Northern girls.
    
    ROS: Did you hear the king’s in Winterfell?
    
    TYRION: I did hear something about that.
    
    ROS: And the queen. And her twin brother. They say that he is the most handsome man in the Seven Kingdoms.
    
    TYRION: And the other brother?
    
    ROS: The queen has two brothers?
    
    TYRION: There’s the pretty one. And there’s the clever one.
    
    ROS: I hear they call him the Imp.
    
    TYRION: I hear he hates that nickname.
    
    ROS: Oh? I hear he’s more than earned it. I hear he’s a drunken little lecher into all manner of perversions.
    
    TYRION: Clever girl.
    
    ROS: We’ve been expecting you, Lord Tyrion.
    
    TYRION: Have you?
    
    TYRION: The gods gave me one blessing.
    
    [She climbs on TYRION. JAIME walks in without knocking.]
    
    JAIME: Don’t get up.
    
    ROS: M’lord.
    
    TYRION: Should I explain to you the meaning of a closed door in a whorehouse, brother?
    
    JAIME: You’ve much to teach me, no doubt. But our sister craves your attention.
    
    TYRION: She has odd cravings, our sister.
    
    JAIME: A family trait. Now, the Starks are feasting us at sundown. Don’t leave me alone with these people.
    
    TYRION: I’m sorry, I’ve begun the feast a bit early. And this is the first of many courses.
    
    JAIME: I thought you might say that. But since we’re short on time, (he opens the door; a bevy of whores enter and descend on TYRION) Come on, girls. See you at sundown.
    
    [JAIME leaves.]
    
    TYRION: Close the door!
    
    Scene changes to the Winterfell crypt, at Lyanna’s tomb. [Robert places a feather in the hand of her statue.]
    
    ROBERT: Did you have to bury her in a place like this? She should be on a hill somewhere with the sun and the clouds above her.
    
    NED: She was my sister. This is where she belongs.
    
    ROBERT: She belonged with me.
    
    [He touches Lyanna’s face.]
    
    ROBERT: In my dreams, I kill him every night.
    
    NED: It’s done, Your Grace. The Targaryens are gone.
    
    ROBERT: Not all of them.
    
    [Scene shifts to Daenerys on a balcony in Pentos, across the Narrow Sea.]
    
    VISERYS (off camera): Daenerys!
    
    [He enters a large chamber.]
    
    VISERYS: Daenerys! There’s our bride to be! Look – a gift from Illyrio. Touch it. Come on. Feel the fabric. Mmmm. Isn’t he a gracious host?
    
    DAENERYS: We’ve been his guests for over a year and he’s never asked us for anything.
    
    VISERYS: Illyrio is no fool. He knows I won’t forget my friends when I come into my throne. You still slouch. Let me see. (He pulls off her gown.) You have a woman’s body now. (She endures it as he strokes her breast.) I need you to be perfect today. Can you do that for me? You don’t want to wake the dragon, do you?
    
    DAENERYS: No.
    
    [VISERYS nods and starts to leave the chamber. He turns.]
    
    VISERYS: When they write the history of my reign, sweet sister, they will say it began today.
    
    [Daenerys turns and steps into a steaming hot bath with a despairing look on her face.]
    
    MAID: It’s too hot, my lady.
    
    [But DAENERYS keeps stepping deeper. The scene shifts to ILLYRIOS, DAENERYS, AND VISERYS outside the mansion, awaiting Khal Drogo.]
    
    VISERYS: Where is he?
    
    ILLYRIO: The Dothraki are not known for their punctuality.
    
    [A host of Dothraki come riding up. Khal Drogo wheels his stallion into the front.]
    
    ILLYRIO: (Greets them in Dothraki.) May I present my honored guests? Viserys of House Targaryen, the third of his name. The rightful King of the Andals and the First Men. And his sister, Daenerys, of the House Targaryen.
    
    VISERYS (to DAENERYS) Do you see how long his hair is? When Dothraki are defeated in combat, they cut off their braid so the whole world can see their shame. Khal Drogo has never been defeated. He’s a savage, of course, but he’s one of the finest killers alive. And you will be his queen.
    
    ILLYRIO: Come forward, my dear.
    
    [KHAL DROGO watches as DAENERYS walks toward him. She does not hesitate and looks straight at him, although there is fear on her face. KHAL DROGO gazes at her and then leads his horsemen on a charge away.]
    
    VISERYS: Where’s he going?
    
    ILLYRIO: The ceremony is over.
    
    VISERYS: But he didn’t say anything. Did he like her?
    
    ILLYRIO: Trust me, Your Grace. If he didn’t like her, we’d know.
    
    [The scene shifts to ILLYRIO, VISERYS, AND DAENERYS ON A GARDEN BALCONY OVERLOOKING THE SEA.]
    
    ILLYRIO: It won’t be long now. Soon you will cross the Narrow Sea and take back your father’s throne. The people drink secret toasts to your health. They cry out for their true king.
    
    VISERYS: When will they be married?
    
    ILLYRIO: Soon. The Dothraki never stay still for long.
    
    VISERYS: Is it true they lie with their horses?
    
    ILLYRIO: I wouldn’t ask Khal Drogo.
    
    VISERYS: Do you take me for a fool?
    
    ILLYRIO: I take you for a king. Kings lack the caution of common men. My apologies if I’ve given offense.
    
    VISERYS: I know how to play a man like Drogo. I give him a queen and he gives me an army.
    
    DAENERYS (pleadingly) I don’t want to be his queen. I want to go home.
    
    VISERYS: So do I. I want us both to go home. But they took it from us. So tell me, sweet sister, how do we go home?
    
    DAENERYS: I don’t know.
    
    VISERYS: We go home with an army. With Khal Drogo’s army. I would let his whole tribe fuck you, all 40,000 men and their horses too, if that’s what it took.
    
    [He gives DAENERYS a brotherly kiss on the forehead and walks away. The scene shifts to a bedroom in Winterfell, where CATELYN is fixing SANSA’S hair.]
    
    SANSA: Do you think Joffrey will like me? What if he thinks I’m ugly?
    
    CATELYN: Then he is the stupidest prince that ever lived.
    
    SANSA: He’s so handsome.
    
    [CATELYN rolls her eyes.]
    
    SANSA: When would we be married? Soon or do we have to wait?
    
    CATELYN: Hush now. Your father hasn’t even said yes.
    
    SANSA: Why would he say no? He’d be the second most powerful man in the kingdoms.
    
    CATELYN: He’d have to leave home. He’d have to leave me. And so would you.
    
    SANSA: You left your home to come here. And I’d be queen someday. Please make father say yes.
    
    CATELYN: Sansa…
    
    SANSA: Please, please. It’s the only thing I ever wanted.
    
    [Scene shifts to the Winterfell banquet. Laughter, music, KING ROBERT getting bawdy with a wench. CATELYN and CERSEI watch, CATELYN embarrassed for CERSEI, who looks disgusted. Out in the courtyard, JON takes out his frustration on a fencing dummy. His uncle BENJEN rides up.]
    
    BENJEN: Is he dead yet?
    
    JON: Uncle Benjen!
    
    [They hug.]
    
    BENJEN: You got bigger. I rode all day. Didn’t want to leave you alone with the Lannisters. Why aren’t you at the feast?
    
    JON: Lady Stark thought it might insult the royal family to seat a bastard in their midst.
    
    BENJEN: Well, you’re always welcome on the wall. No bastard was ever refused a seat there.
    
    JON: So take me with you when you go back.
    
    BENJEN: Jon…
    
    JON: Father will let me if you ask him, I know he will.
    
    BENJEN: The Wall isn’t going anywhere.
    
    JON: I’m ready to swear your oath.
    
    BENJEN: You don’t understand what you’d be giving up. We have no families. None of us will ever father sons.
    
    JON: I don’t care about that.
    
    BENJEN: You might, if you knew what it meant. … I’d better get inside. Rescue your father from his guests. We’ll talk later.
    
    [BENJEN goes to the banquet.]
    
    TYRION: Your uncle’s in the Night’s Watch.
    
    JON: What’re you doing back there?
    
    TYRION (drinking): Preparing for a night with your family. I’ve always wanted to see the Wall.
    
    JON: You’re Tyrion Lannister. The queen’s brother?
    
    TYRION: My greatest accomplishment. You – you’re Ned Stark’s bastard, aren’t you?
    
    [JON looks angry and turns away.]
    
    TYRION: Did I offend you? Sorry. You are the bastard, though.
    
    JON: Lord Eddard Stark is my father.
    
    TYRION: And Lady Stark is not your mother. Making you a bastard. Let me give you some advice, bastard. Never forget what you are. The rest of the world will not. Wear it like armor. Then it can never be used to hurt you.
    
    JON: What the hell do you know about being a bastard?
    
    TYRION: All dwarves are bastards in their fathers’ eyes.
    
    [TYRION departs. JON picks up his sword and attacks the dummy with new ferocity.]
    
    [The scene shifts back to the banquet, in full raucous swing. NED is off to himself; BENJEN comes up to him.]
    
    BENJEN: You at a feast -- It’s like a bear in a trap.
    
    NED: The boy I beheaded. Did you know him?
    
    BENJEN: Of course I did. Just a lad. But he was tough, Ned. A true Ranger.
    
    NED: He was talking madness. Said the Walkers slaughtered his friends.
    
    BENJEN: The two he was with are still missing.
    
    NED: A wildling ambush.
    
    BENJEN: Maybe. Direwolves south of the wall. Talk of the Walkers. My brother might be the next Hand to the king. Winter is coming.
    
    NED: Winter is coming.
    
    [ROBB approaches.]
    
    ROBB: Uncle Benjen.
    
    BENJEN: Robb boy. How are ye?
    
    ROBB: I’m good.
    
    [KING ROBERT gets even more bawdy with a wench.]
    
    CATELYN (in desperation) Is this your first time in the North, Your Grace?
    
    CERSEI: Yes. Lovely country.
    
    [They observe SANSA.]
    
    CATELYN: I’m sure it’s very grim, after Kings Landing. I remember how scared I was when Ned brought me up here for the first time.
    
    [SANSA approaches and smiles shyly at CERSEI.]
    
    CERSEI: Hello, little dove. But you are a beauty. How old are you?
    
    SANSA: Thirteen, Your Grace.
    
    CERSEI: You’re tall. Still growing?
    
    SANSA: I think so, Your Grace.
    
    CERSEI: And have you bled yet?
    
    SANSA (discomfited): No, Your Grace.
    
    CERSEI: And your dress. Did you make it?
    
    [SANSA nods yes.]
    
    CERSEI: Such talent. You must make something for me.
    
    [SANSA departs.]
    
    CERSEI (to CATELYN): I hear we might share a grandchild someday.
    
    CATELYN: I hear the same.
    
    CERSEI: Your daughter will do well in the capital. Such a beauty shouldn’t stay hidden up here forever.
    
    [SANSA and JOFFREY catch each other’s eye. JOFFREY smiles at her and she turns to her friend.]
    
    [JAIME and NED meet up. JAIME blocks their path.]
    
    NED: Your pardon.
    
    JAIME: I hear we might be neighbors soon. I hope it’s true.
    
    NED: Yes, the king has honored me with his offer.
    
    JAIME: I’m sure we’ll have a tournament to celebrate the new title, if you accept. It would be good to have you in the field. The competition has become a bit stale.
    
    NED: I don’t fight in tournaments.
    
    JAIME: No? Getting a little old for it?
    
    NED: I don’t fight in tournaments because when I fight a man for real, I don’t want him to know what I can do.
    
    JAIME: Well said.
    
    [ARYA flips food onto SANSA’s face.]
    
    SANSA: Arya!
    
    [CATELYN signals a laughing ROBB to deal with the girls. He hoists up ARYA.]
    
    ROBB: Time for bed.
    
    [The scene shifts to after the banquet. NED and CATELYN are in their bed.]
    
    NED: I’m a Northman. I belong here with you, not down south in that rat’s nest they call a capital.
    
    CATELYN: I won’t let him take you.
    
    NED: The king takes what he wants. That’s why he’s king.
    
    CATELYN: I’ll say, ‘Listen, fat man, you are not taking my husband anywhere. He belongs to me now.’
    
    NED: How did he get so fat?
    
    CATELYN: He only stops eating when it’s time for a drink.
    
    [There’s a knock at the door.]
    
    A VOICE: It’s Maester Luwin, my lord.
    
    NED: Send him in.
    
    LUWIN: Pardon, my lord, my lady. A rider in the night from your sister.
    
    [He hands CATELYN a sealed note.]
    
    NED: Stay.
    
    CATELYN: This was sent from the Eyrie. What’s she doing at the Eyrie? She hasn’t been back there since her wedding.
    
    [CATELYN reads the note, looks up in alarm, and then burns it.]
    
    NED: What news?
    
    CATELYN: She’s fled the capital. She says Jon Arryn was murdered. By the Lannisters. She says the king is in danger.
    
    NED: She’s fresh widowed, Cat. She doesn’t know what she’s saying.
    
    CATELYN: Lysa’s head would be on a spike right now if the wrong people had found that letter. Do you think she would risk her life, her son’s life, if she wasn’t certain her husband was murdered?
    
    LUWIN: If this news is true, and the Lannisters conspire against the throne, who but you can protect the king?
    
    CATELYN: They murdered the last Hand. Now you want Ned to take the job.
    
    LUWIN: The king rode for a month to ask Lord Stark’s help. He’s the only one he trusts. You swore the king an oath, my lord.
    
    CATELYN: He spent half his life fighting Robert’s wars. He owes him nothing. (To NED) Your father and brother rode south once on a king’s demand.
    
    LUWIN: A different time. Different king.
    
    [The scene shifts to the wild wedding celebration of KHAL DROGO and DAENERYS. Fighting and fornication. DAENERYS looks stricken at everything around her.]
    
    VISERYS: When do I meet with the Khal? We need to begin planning the invasion.
    
    ILLYRIO: If Khal Drogo has promised you a crown, you shall have it.
    
    VISERYS: When?
    
    ILLYRIO: When their omens favor war.
    
    VISERYS: I piss on Dothraki omens. I waited 17 years to get my throne back.
    
    [The sex and violence intensify. Two men fight to the death over a woman each is trying to rape. KHAL DROGO watches avidly.]
    
    ILLYRIO: A Dothraki wedding without at least three deaths is considered a dull affair.
    
    [A knight in Westerosi garb appears. KHAL DROGO greets him in Dothraki. It is JORAH MORMONT, bearing books.]
    
    JORAH: A small gift for the new Khaleesi. Songs and histories from the Seven Kingdoms.
    
    DAENERYS: Thank you, ser. Are you from my country?
    
    JORAH: Ser Jorah Mormont of Bear Island. I served your father for many years. Gods be good, I hope to always serve the rightful king.
    
    [DANY is presented with a chest with three dragon eggs in it.]
    
    ILLYRIO: Dragons’ eggs, Daenerys. From the Shadow Lands beyond Asshai. The ages have turned them to stone, but they will always be beautiful.
    
    DAENERYS: Thank you, Magister.
    
    [KHAL DROGO rises and strides forward. DAENERYS follows him, looking sick with fear. The Dothraki crowd behind her as she goes. The KHAL leads her to a white mare.]
    
    DAENERYS: She’s beautiful. … Ser Jorah, I don’t know how to say ‘thank you’ in Dothraki.
    
    JORAH: There is no word for ‘thank you’ in Dothraki.
    
    [The KHAL puts DANY on her horse and mounts his.]
    
    VISERYS: Make him happy.
    
    [The scene shifts to the seaside at sunset. The KHAL begins to unwrap DANY’s dress. She is sobbing. He touches the tears on her face.]
    
    KHAL DROGO: No.
    
    DAENERYS: Do you know the Common Tongue?
    
    KHAL DROGO: No.
    
    DAENERYS: Is ‘no’ the only word that you know?
    
    KHAL DROGO: No.
    
    [He takes off her gown and bends her down.]
    
    [The scene shifts to Winterfell. Tyrion and the Hound are seated outside the day after the banquet.]
    
    THE HOUND: Rough night, Imp?
    
    TYRION: If I get through this without squirting from one end or the other, it will be a miracle.
    
    THE HOUND: I didn’t pick you for a hunter.
    
    TYRION: The greatest in the land. My spear never misses.
    
    THE HOUND: It’s not hunting if you pay for it.
    
    [The king and Ned come into view.]
    
    ROBERT: Are you as good with a spear as you used to be?
    
    NED: No, but I’m still better than you.
    
    ROBERT: I know what I’m putting you through. Thank you for saying yes. I only ask you because I need you. You’re a loyal friend. You hear me? A loyal friend. The last one I’ve got.
    
    NED: I hope I’ll serve you well.
    
    ROBERT: You will. And I’ll make sure you don’t look so fucking grim all the time. Come on, boys, let’s go kill some boar!
    
    [The king’s party rides off, NED nodding goodbye to BRAN, whose wolf pup begins sniffing at his feet.]
    
    BRAN: Come on, you.
    
    [BRAN begins climbing, his wolf pup crying at the bottom of the castle wall. As he nears the top, he hears a woman and man moaning. Peering in the window, he sees CERSEI and JAIME having sex. CERSEI sees BRAN.]
    
    CERSEI: Stop. STOP.
    
    [JAIME runs and grabs BRAN at the window.]
    
    JAIME: Are you completely mad?
    
    CERSEI: He saw us.
    
    JAIME: It’s all right. It’s all right.
    
    CERSEI: He saw us!
    
    JAIME: I heard you the first time. (To BRAN) Quite the little climber, aren’t you? How old are you, boy?
    
    BRAN: Ten
    .
    JAIME: Ten.
    
    [JAIME looks at CERSEI, who gazes back imploringly.]
    
    JAIME: The things I do for love.
    
    [He shoves BRAN out the window.]
    
    [ending]
    
    
    
    
    10
    
    Embed
    About
    Genius Annotation
    3 contributors
    
    
    The first episode of the Game of Thrones series starts, typically, in the icy cold beyond the wall. Things don’t get any warmer as we meet the show’s characters for the first time.
    
    The plot (Released by HBO): Lord Stark is troubled by reports from a Night’s Watch deserter; King Robert and the Lannisters arrive at Winterfell; Viserys Targaryen forges a new alliance.
    
    The title is a reference to the motto of the house Stark “Winter Is Coming”.
    
    +2
    
    1
    
    
    Share
    Ask us a question about this song
     
    Ask a question *
    Season 1 Scripts (2011)
    Game of Thrones
    1.
    Winter is Coming
    2.
    The Kingsroad
    3.
    Lord Snow
    4.
    Cripples, Bastards and Broken Things
    5.
    The Wolf and the Lion
    6.
    A Golden Crown
    7.
    You Win or You Die
    8.
    The Pointy End
    9.
    Baelor
    10.
    Fire and Blood
    Credits
    Produced By
    D.B. Weiss & David Benioff
    Written By
    D.B. Weiss & David Benioff
    Actors
    Emilia Clarke, Kit Harington, Nikolaj Coster-Waldau, Lena Headey, Maisie Williams, Iain Glen, Alfie Allen, Sophie Turner, Isaac Hempstead Wright, Sean Bean, Mark Addy, Michelle Fairley, Jason Momoa, Kristian Nairn, Harry Lloyd, Jack Gleeson, Art Parkinson & Rory McCann
    Distributor
    HBO
    Production Companies
    Bighead Littlehead, Generator Entertainmen, Grok! Studio, Television 360 & HBO
    Directed By
    Tim Van Patten
    Release Date
    April 17, 2011
    Tags
    Non-Music
    TV
    Screen
    Expand 
    Comments
    Add a comment
    martin
    3 years ago
    Piano tutorial to the Main Theme, great!
    
    navanathvalankewar
    9 months ago
    How to download free
    
    Expand 
    Sign Up And Drop Knowledge 🤓
    Genius is the ultimate source of music knowledge, created by scholars like you who share facts and insight about the songs and artists they love.
    Sign Up
    Genius is the world’s biggest collection of song lyrics and musical knowledge
    About Genius
    Contributor Guidelines
    Press
    Shop
    Advertise
    Event Space
    Privacy Policy
    Licensing
    Jobs
    Developers
    Copyright Policy
    Contact Us
    Sign In
    Do Not Sell My Personal Information
    © 2022 Genius Media Group Inc.
    Terms of Use
    VERIFIED ARTISTS
    ALL ARTISTS:
    A
    B
    C
    D
    E
    F
    G
    H
    I
    J
    K
    L
    M
    N
    O
    P
    Q
    R
    S
    T
    U
    V
    W
    X
    Y
    Z
    #
    HOT SONGS:
    藤井風 (FUJII KAZE) - 死ぬのがいいわ (SHINUNOGA E-WA) (ROMANIZED)
    ПО КРЫШАМ (OVER THE ROOFS)
    POLAND
    ТЕСНО (TIGHT)
    CASE 143
    VIEW ALL
    
    


```python
#save the webpage as text file
f_test=open("S1E1.txt","w", encoding='utf-8') 

for string in page.strings:
    f_test.write(string)

f_test.close()
```


```python
#open the script
with open("S1E1.txt",encoding='utf-8',errors='ignore') as f:
         data = f.read()
#print the data(if applicable) 
#print(data)
```


```python
#data cleaning: remove the inequivalent contents

#type the "[begining]" and the "[ending]" between the content we want(edit directly in txt file)
#remove the text above "[begining]"
data = data.split('[begining]')[1]
#print the data(if applicable) 
#print(data)
```


```python
#remove the text below "[ending]"
data = data.split('[ending]')[0]
#print the data(if applicable) 
#print(data)
```


```python
#get rid of the "-" in the script
data = data.replace('-', '')
#print the data(if applicable) 
#print(data)
```


```python
#remove all the blank lines in the script
regex = r"^\s+$"
subst = ""
data = re.sub(regex, subst, data, 0, re.MULTILINE)

regex = r"^$\n"
subst = ""
data = re.sub(regex, subst, data, 0, re.MULTILINE)

#print the data(if applicable) 
#print(data)
```


```python
#save the cleaned script for later use of wordcloud
f_2=open("word_cloudS1E1.txt","w", encoding='utf-8') 
f_2.write(data)
f_2.close()
```


```python
#split the lines by the line changing mark
lines = data.split('\n')
#print the data(if applicable) 
#print(data)
```


```python
#number the lines
myrows = []

num = 1
for line in lines:
    myrows.append([num, line])
    num = num + 1
#check whether the lines have been successfully splited and numbered
myrows[:10]
```




    [[1,
      '[First scene opens with three Rangers riding through a tunnel, leaving the Wall, and going into the woods. (Eerie music in background) One Ranger splits off and finds a campsite full of mutilated bodies, including a child hanging from a tree branch. A birdseye view shows the bodies arranged in a shieldlike pattern. The Ranger rides back to the other two.]'],
     [2,
      'WAYMAR ROYCE: What d’you expect? They’re savages. One lot steals a goat from another lot and before you know it, they’re ripping each other to pieces.'],
     [3,
      'WILL: I’ve never seen wildlings do a thing like this. I’ve never seen a thing like this, not ever in my life.'],
     [4, 'WAYMAR ROYCE: How close did you get?'],
     [5, 'WILL: Close as any man would.'],
     [6, 'GARED: We should head back to the wall.'],
     [7, 'ROYCE: Do the dead frighten you?'],
     [8,
      'GARED: Our orders were to track the wildlings. We tracked them. They won’t trouble us no more.'],
     [9,
      'ROYCE: You don’t think he’ll ask us how they died? Get back on your horse.'],
     [10, '[GARED grumbles.]']]




```python
#turn the numbered and splited lines into dataframe
df = pd.DataFrame(myrows)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>[First scene opens with three Rangers riding t...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>WAYMAR ROYCE: What d’you expect? They’re savag...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>WILL: I’ve never seen wildlings do a thing lik...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>WAYMAR ROYCE: How close did you get?</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>WILL: Close as any man would.</td>
    </tr>
  </tbody>
</table>
</div>




```python
#name the column
df.columns = ['line', 'text']
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>line</th>
      <th>text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>[First scene opens with three Rangers riding t...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>WAYMAR ROYCE: What d’you expect? They’re savag...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>WILL: I’ve never seen wildlings do a thing lik...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>WAYMAR ROYCE: How close did you get?</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>WILL: Close as any man would.</td>
    </tr>
  </tbody>
</table>
</div>




```python
#save the data frame to csv.file
df.to_csv('dataS1E1.csv', index=False,encoding='utf-16')
```

import streamlit as st
from app import create_image_text_layout   # reuse function from main.py

def display_content():

    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
    h2 {
        font-family: 'UnifrakturCook', cursive !important;
        font-size: 48px;
        text-align: center;
        color: #e7b66c !important;
    }
    p, li { 
        font-size: 18px !important;
        # line-height: 1.6 !important;
        text-align: justify !important;
        color: oldlace;
    }

    table {
        border-collapse: collapse;
        width: 100%;
    }

    td {
        border: 2px solid #444 !important;
        padding: 5px;
        font-size: 16Fpx !important;
        line-height: 1.2 !important;
        text-align: justify !important;
        color: oldlace;
        background-color: #6969691f; /* dark background to contrast oldlace */
    }


    .beth1 {
            font-family: 'Beth Ellen', cursive !important; /* <-- use Beth Ellen (imported) */
            font-size: 22px;
            color: oldlace !important;
            text-align: center !important;
            margin-top: 0.2em;
            color: dimgray !important;
        }

    </style>
    """,
    unsafe_allow_html=True
    )
    create_image_text_layout("attached_assets/generated_images/chap7main.jpg", layout="full")


    text0 = """
    <h2>Chapter 7: The Spark Against Wahid </h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    text1 = """
    <p>"<span style="color:#FF5733;">Kuch battles me tum haarte nahi, tum bas gayab ho jaate ho.</span>" Malik… gayab ho gaya."
    Kabhi kabhi zindagi me jeet ka matlab kisi ko haarana nahi, balki unke dil me ek aisa aaina rakh dena hota hai, jisme wo apna asli chehra dekh sakein. 
    Malik ka khel khatam ho chuka tha.
Vo ab underground tha — jaise ek aisa shikari jo khud shikaar ban gaya ho.
Uske paas koi raasta nahi bacha tha… har taraf uski audio leke log ghoom rahe the, uske naam ke charche har gali-mehfil me chal rahe the.

Situation clear thi:
<span style="color:#FF5733;">"Jab halat tumhe maarne lage, toh kabhi kabhi jeet isme hoti hai ki tum bas dikhai na do."</span> Malik ne wahi kiya — underground ho gaya.
"Game me next piece move karne ka time aa gaya tha… aur iss baar target tha Wahid."
Ye move ek Sequential Strategy hai (Game Theory) — ek enemy ko neutralise karke dusre pe focus karna.
maine ye samjha ki group ka balance todne ke liye, Influence Hub (Wahid) ko dismantle karna zaroori hai.
"Chess me King ko mat maaro, uske Bishops aur Knights tod do, King khud gir jayega."
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap71.jpg", text1, layout="side", image_position="right")


    text111 = """
Malik hat chuka tha, ab meri list me doosra naam tha — Wahid.
Yahaan ek Mushkil Task tha — do jodo ko todna (two pairs ko alag karna).
Par pehla step mere liye apni khud ki image ko recover karna tha.

Maine shuru kiya apna <span style="color:#FF5733;">Emotional Game</span> — soft corner banana, purani yaadein jagana, sacrifice ka zikr karna.
maine Nostalgia Trigger kiya — science ke hisaab se nostalgia insaan ka trust hormone (oxytocin) boost karta hai.
maine Wahid ke mind me ek safe-space feeling banayi, taaki resistance kam ho.
Ye ek classic Foot-in-the-Door tactic hai — pehle small emotional favour, phir bigger influence.
"Insaan facts se nahi, apne emotions ke saath loyal hota hai."
Wahid se bola:
"Main tujhe kabhi chhodna nahi chahta tha… samajh bhai, main tere liye kitna khada raha."
    """
    create_image_text_layout(text_content=text111, layout="full")




    text11 = """
    <p>
Purani kahaniyaan, old memories, old sacrifices — sab remind karva diye. Wahi game maine Karishma ke liye kiya — lekin is baar <span style="color:#FF5733;">it was real.</span>
Aur dheere-dheere hum teeno — Tahir, Wahid, Karishma — ek normal bonding pe aa gaye.

main ek Dual Channel Influence bana rahe the — Wahid ke saath emotional connect, Karishma ke saath sympathy connect.
Isse mera Control Graph bana:
Wahid — Karishma (sab indirectly tumse connected).
"Jab tum dono sides ke doston ke dost ban jaate ho, tumhara word gold ban jaata hai."

<span style="color:#FF5733;">Sab normal lagne laga… but mere andar ka shikari kabhi soya nahi."</span>"
Lekin mera chanchal mann phir se activate ho gaya.
Mann mujhse bola: bhool gaya wo din jab Wahid ne mujhse jhoot bola tha…
Bhool gaya jab vo sabha jb usne mere 6 saal purane dost ko gaali di thi…
Bhool gaya jab usne Karishma ke saamne mujhe bura dikhaya tha.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap72.jpg", text11, layout="side", image_position="left")


    text1111 = """
mere brain ne ek Delayed Revenge Loop activate kiya — jaise hi maine emotionally safe feel kiye, subconscious ne mujhe original goal yaad dilaya.
Ye Anchored Memory hai — jo tab tak silent hoti hai jab tak emotional environment safe na ho.

Main psychology me manta hoon:
"<span style="color:#FF5733;">Insaan dimaag se nahi, apne emotions ke filter se yaad rakhta hai.</span> Jo emotions thande ho jaate hain, unke saath memory bhi fade ho jaati hai."
Ab mujhe laga — game dobara shuru karna padega.
Plan simple tha — Uske past me jaana.
Jo chiz usne chhupayi hai, wahi uski kamzori banegi.
"Jo hua, bhool gaya tha… par bhoolne ka matlab maaf karna nahi hota."
    """
    create_image_text_layout(text_content=text1111, layout="full")



    text2 = """
    <p>
Maine usse purani kahani sunwayi aur dhire-dhire uska old server, old yaadein nikalwa li.
Wo jagah jahan uske purane dosto ki kahaniyaan thi.

maine Self-Disclosure Trap use kiya — kisi se unka past khud bulwana unke ego ko satisfy karta hai (“Main apna history share kar raha hu”), lekin is process me mera kaam ho jaata hai.
Past memories = past weaknesses = future weapons.
"Jab tum kisi ka past jaan jaate ho, tum unka future predict kar sakte ho."


Is process me maine dekha ki uski koi permanent male friendship nahi thi.
Lekin ek female — Rina — mujhe alag lagi.
Mature, <span style="color:#FF5733;">jimmedar</span>, vibes match.

Lekin mera rule tha:
"<span style="color:#FF5733;">"Apne war me kisi innocent ko pawn mat banao."</span>
Ye meri Ethical Boundary hai — matlab tum apni strategy me ek limit maintain karte ho.
Ye important hai kyunki Over-Manipulation backfire kar sakta hai
So, I stopped that track. Wahid past mere saamne tha… aur main jaanta tha — “Har insaan apne past me apna sabse bada weakness chhod ke jaata hai.”
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap73.jpg", text2, layout="side", image_position="right")




    text22 = """
Ek din Karishma se suna — Wahid aur uske beech kuch theek nahi chal raha.
Mere andar ek twisted khushi thi — jo chaha tha, wahi ho raha tha.
Par saath me ek sadness — kyunki Karishma hurt thi.
Ye mera Confirmation Bias moment tha — main already expect kar rahe the ki ye relation tootega, aur jab proof mila, mera confidence double ho gaya. Karishma ne mujhe kaha ki usse badla lena hai. Bade bhai hone ke nate, maine usse yeh sab karne ki salah nahi di. Bhai ke hote hue bhala ek nari ranbhoomi mein kyun utare?

maine immediately us emotional gap ka benefit liya.
"Relationship me crack aane ka wait mat karo, jab crack aaye to usme wedge daal do."
Jab reason pata chala — Wahid ki baat uski ex se ho rahi thi — mujhe clarity mil gayi:
<span style="color:#FF5733;">"Jo aadmi loyalty me fail ho, wo har relation me fail hota hai."</span>
Main ne decide kiya ki main double role play karunga:
    """
    create_image_text_layout(text_content=text22, layout="full")



    text3 = """
    <p>
Wahid ko force karna, ki baat kar Karishma se. Baar-baar force karne ki baat kar, baat kar, baat kar… isse hota yeh hai ki tum woh cheez nahi karte jo tumse forcefully karai jaye — jaise main samjha raha hu.
Karishma ko real motive se samjhana ki ye ladka galat hai.
<span style="color:#FF5733;">Ek taraf push, ek taraf protect.</span>
Yahi hota hai mind game ka art — “Ek haath se todna, dusre se sambhalna.”
Main ne Wahid ko kaha:
"Cheat mat kar, tu galat kar raha hai… jo tere saath hua, tu wahi uske saath karega?"

Ye ek Push-Pull Strategy hai — ek taraf se trust break karwana, doosri taraf se emotional safety provide karna.
Result: Wahid guilt + Karishma dependency on you.

Aur Karishma ko samjhaya:
"Jo dhokhe se shuru hota hai, wo dhokhe pe khatam hota hai.",
"<span style="color:#FF5733;">Jo dhoke se paida hota hai, relationship me dhoka hi deta hai</span>",
"Kisi ke past ke trauma ko heal karne ke liye apne present me naye trauma mat create karo." ...

Mujhe pata chala Rina hi mediator hai jo Wahid aur uski ex (Razzi) ko connect kar rahi hai.
Mere mann me ek thought aaya — kash ye mujhe Razzi se milwa de.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap74.jpg", text3, layout="side", image_position="left")


    text5 = """
    <p>

Nature ne game kheli — bina maange Razzi VC me aa gayi jab main Rina ke saath tha.
Wahid ne mujhe wahan dekha — <span style="color:#FF5733;">insecurity trigger.</span>
Ye ek Jealousy Trigger tha — jealousy insaan ko irrational bana deti hai, jo tumhara goal tha.
maine uska stability pillars tod diye — Rina, main, aur Karishma — teenon ke saath uska connection disrupt ho gaya.

Result — mujhse baat bandh, Rina se bhi baat bandh.
Kuch din baad main dobara emotional care mode me aaya, Wahid se baat resume.
Phir double role — Wahid ko push, Karishma ko heal.
Ek din dekha Wahid aur Razzi VC me.
Maine Karishma ko proof bheja — "Dekho kya kar raha hai."
Server ka public link save kiya pehle se, kyunki mujhe pata tha kick milega.

Ye Shock Therapy tha — sudden undeniable evidence dekar maine Karishma ka trust permanently Wahid se tod diya.
maine apna access bhi secure rakha (server link save) — matlab maine future infiltration ka option open rakha.

Plan — jab teeno ek jagah honge, solution niklega. Lekin unexpected — Karishma ne trauma se bachne ke liye Malik ki tarah <span style="color:#FF5733;">underground hona decide kiya.</span> 1 week gayab — mene socha iska matlab Game Won hai.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap75.jpg", text5, layout="side", image_position="right")




    text6 = """
    <p>
    Mere dimaag me ek soch: "Jo tum dusron ke saath karte ho, wahi tumhare saath hota hai — bas form badal ke." Wahid ke paas ab na mediator tha, na dono taraf ka trust.
    Ye meri indirect win thi — maine enemy ke strongest emotional link ko remove kar diya.
    Wahid ke paas ab koi Emotional Anchor nahi tha.
    "Jab tum kisi ke anchor ko kaat dete ho, wo khud hi drift ho jaata hai."<br><br>
    Game jeet liya tha, lekin justice pending thi. "<span style="color:#FF5733;">Dard ka balance hona chahiye</span> — jitna usne Karishma ko diya, utna usko milna zaroori hai." Jitna tune rulaya hai, utna tu bhi roega.
    <br>
    Psychology Lesson:</p>
    <ul>
    <li>Selective Memory – Emotions decide what we remember.</li>
    <li>Leverage Weakness – Past trauma is the biggest emotional handle.</li>
    <li>Third-Party Influence – Relationships me mediator ka role dangerous hota hai.</li>
    <li>Reverse Triggering – Kabhi kabhi kisi ko apna asli chehra dikhane ka best tareeka hota hai unhe apni insecurity se rubaru karwana.</li>
    </ul>
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap76.jpg", text6, layout="side", image_position="left")



    create_image_text_layout("attached_assets/generated_images/chap7ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>Forgiving is not the same as forgetting — and forgetting is never the same as forgiving. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 
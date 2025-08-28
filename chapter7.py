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


#     text1 = """
#     <p>"Kuch battles me tum haarte nahi, tum bas gayab ho jaate ho. Malik… gayab ho gaya."
#     Kabhi kabhi zindagi me jeet ka matlab kisi ko haarana nahi, balki unke dil me ek aisa aaina rakh dena hota hai, jisme wo apna asli chehra dekh sakein. 
#     Malik ka khel khatam ho chuka tha.
# Vo ab underground tha — jaise ek aisa shikari jo khud shikaar ban gaya ho.
# Uske paas koi raasta nahi bacha tha… har taraf uski audio leke log ghoom rahe the, uske naam ke charche har gali-mehfil me chal rahe the.

# Situation clear thi:
# "Jab halat tumhe maarne lage, toh kabhi kabhi jeet isme hoti hai ki tum bas dikhai na do." Malik ne wahi kiya — underground ho gaya.
# "Game me next piece move karne ka time aa gaya tha… aur iss baar target tha Wahid."
# Malik hat chuka tha, ab meri list me doosra naam tha — Wahid.
# Yahaan ek Mushkil Task tha — do jodo ko todna (two pairs ko alag karna).
# Par pehla step mere liye apni khud ki image ko recover karna tha.

# Maine shuru kiya apna Emotional Game — soft corner banana, purani yaadein jagana, sacrifice ka zikr karna.
# Wahid se bola:
# "Main tujhe kabhi chhodna nahi chahta tha… samajh bhai, main tere liye kitna khada raha."
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text1, layout="side", image_position="right")



#     text11 = """
#     <p>
# Purani kahaniyaan, old memories, old sacrifices — sab remind karva diye. Wahi game maine Karishma ke liye kiya — lekin is baar it was real.
# Aur dheere-dheere hum teeno — Tahir, Wahid, Karishma — ek normal bonding pe aa gaye.
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text11, layout="side", image_position="left")



#     text2 = """
#     <p>
# Lekin mera chanchal mann phir se activate ho gaya.
# Main bhool gaya wo din jab Wahid ne mujhse jhoot bola tha…
# Bhool gaya jab usne mere 6 saal purane dost ko gaali di thi…
# Bhool gaya jab usne Karishma ke saamne mujhe bura dikhaya tha.

# Main psychology me manta hoon:
# "Insaan dimaag se nahi, apne emotions ke filter se yaad rakhta hai. Jo emotions thande ho jaate hain, unke saath memory bhi fade ho jaati hai."

# Ab mujhe laga — game dobara shuru karna padega.
# Plan simple tha — Uske past me jaana.
# Jo chiz usne chhupayi hai, wahi uski kamzori banegi.

# Maine usse purani kahani sunwayi aur dhire-dhire uska old server, old yaadein nikalwa li.
# Wo jagah jahan uske purane dosto ki kahaniyaan thi.
# Is process me maine dekha ki uski koi permanent male friendship nahi thi.
# Lekin ek female — Rina — mujhe alag lagi.
# Mature, jimmedar, vibes match.

# Lekin mera rule tha:
# "Apne war me kisi innocent ko pawn mat banao."
# So, I stopped that track.
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text2, layout="side", image_position="left")


#     text3 = """
#     <p>
# Ek din Karishma se suna — Wahid aur uske beech kuch theek nahi chal raha.
# Mere andar ek twisted khushi thi — jo chaha tha, wahi ho raha tha.
# Par saath me ek sadness — kyunki Karishma hurt thi.

# Jab reason pata chala — Wahid ki baat uski ex se ho rahi thi — mujhe clarity mil gayi:
# "Jo aadmi loyalty me fail ho, wo har relation me fail hota hai."
# Main ne decide kiya ki main double role play karunga:

# Wahid ko force karna ki baat kare Karishma se — jaise main samjha raha hu.

# Karishma ko real motive se samjhana ki ye ladka galat hai.

# Main ne Wahid ko kaha:
# "Cheat mat kar, tu galat kar raha hai… jo tere saath hua, tu wahi uske saath karega?"

# Aur Karishma ko samjhaya:
# "Jo dhokhe se shuru hota hai, wo dhokhe pe khatam hota hai.
# Apne past ke trauma ko heal karne ke liye apne present me naye trauma mat create karo."
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text3, layout="side", image_position="left")


#     text4 = """
#     <p>
# Ek din Karishma se suna — Wahid aur uske beech kuch theek nahi chal raha.
# Mere andar ek twisted khushi thi — jo chaha tha, wahi ho raha tha.
# Par saath me ek sadness — kyunki Karishma hurt thi.

# Jab reason pata chala — Wahid ki baat uski ex se ho rahi thi — mujhe clarity mil gayi:
# "Jo aadmi loyalty me fail ho, wo har relation me fail hota hai."
# Main ne decide kiya ki main double role play karunga:

# Wahid ko force karna ki baat kare Karishma se — jaise main samjha raha hu.

# Karishma ko real motive se samjhana ki ye ladka galat hai.

# Main ne Wahid ko kaha:
# "Cheat mat kar, tu galat kar raha hai… jo tere saath hua, tu wahi uske saath karega?"

# Aur Karishma ko samjhaya:
# "Jo dhokhe se shuru hota hai, wo dhokhe pe khatam hota hai.
# Apne past ke trauma ko heal karne ke liye apne present me naye trauma mat create karo."
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text4, layout="side", image_position="left")

#     text5 = """
#     <p>
# Mujhe pata chala Rina hi mediator hai jo Wahid aur uski ex (Razzi) ko connect kar rahi hai.
# Mere mann me ek thought — kash mujhe Razzi se milwa de.

# Nature ne game kheli — bina maange Razzi VC me aa gayi jab main Rina ke saath tha.
# Wahid ne mujhe wahan dekha — insecurity trigger.
# Result — mujhse baat bandh, Rina se bhi baat bandh.
# Kuch din baad main dobara emotional care mode me aaya, Wahid se baat resume.
# Phir double role — Wahid ko push, Karishma ko heal.
# Ek din dekha Wahid aur Razzi VC me.
# Maine Karishma ko proof bheja — "Dekho kya kar raha hai."
# Server ka public link save kiya pehle se, kyunki mujhe pata tha kick milega.

# Plan — jab teeno ek jagah honge, solution niklega.

# Lekin unexpected — Karishma ne trauma se bachne ke liye Malik ki tarah underground hona decide kiya.
# 1 week gayab — iska matlab Game Won.

# Mere dimaag me ek soch:
# "Jo tum dusron ke saath karte ho, wahi tumhare saath hota hai — bas form badal ke."

# Wahid ke paas ab na mediator tha, na dono taraf ka trust.
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text5, layout="side", image_position="left")


#     text6 = """
#     <p>
# Game jeet liya tha, lekin justice pending tha.
# "Dard ka balance hona chahiye — jitna usne Karishma ko diya, utna usko milna zaroori hai."

# 💡 Psychology Lesson:

# Selective Memory – Emotions decide what we remember.

# Leverage Weakness – Past trauma is the biggest emotional handle.

# Third-Party Influence – Relationships me mediator ka role dangerous hota hai.

# Reverse Triggering – Kabhi kabhi kisi ko apna asli chehra dikhane ka best tareeka hota hai unhe apni insecurity se rubaru karwana.
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap61.jpg", text6, layout="side", image_position="left")



    create_image_text_layout("attached_assets/generated_images/chap6ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>Proof is greater than words; trust and credibility come with evidence, not just claims. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 
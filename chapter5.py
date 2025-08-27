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
    create_image_text_layout("attached_assets/generated_images/chap5main.jpg", layout="full")


    text0 = """
    <h2>Chapter 5: When Realization Demands Resolution</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    text1 = """
    <p>
    Kehte hain,
    "Jis din tumhe pata chale ki tum galat ho, wahi din tum sahi jeena shuru kar dete ho.", “Insaan ki zindagi tab badalti hai jab usse pata chalta hai ki wo galat tha… par asli kahani tab shuru hoti hai jab wo galti sudharne ka faisla karta hai.”
    Par mere liye wo <span style="color:#FF5733;">turning point</span> shanti leke nahi aaya… Wo leke aaya ek <span style="color:#FF5733;">andheraa toofan</span>  — jisme mujhe apna purana roop todna tha… aur ek naya roop banana tha.


    Mujhe yaad hai, sab kuch badla kaise.
    Ek normal sa sham tha. Public VC mein 10-12 log baithe the. Hasna, mazaak, thoda roast, thoda bakwaas — wahi usual scene.
    Aur phir kisi ne mere liye ek teekha sa comment maara. Main jawab dene hi wala tha ki ek awaaz aayi ek awaaz chhapi sab awaazon ke upar — strong, clear, protective.
    Karishma: <span style="color:#FF5733;">Oyee… Tahir ko kuch mat bolna samjhe? ____ ____ kar dungi!</span>.

    Us moment me ek ajeeb si khamoshi mere andar utar gayi.
    Baat sirf shabdon ki nahi thi… baat thi uske tone ki.
    ye sirf words nahi the… ye ek feel thi.
    Uska tone wo normal friendly tone nahi tha — usme ek <span style="color:#FF5733;">Protectiveness</span> thi, ek boundary thi jo usne mere liye draw ki.
    Us pal wo server ki ek member nahi thi… wo meri younger sister thi.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap51.jpg", text1, layout="side", image_position="right")




    text2 = """
    <p>
    Us pal mujhe laga… ye ladki sirf VC ki ek member nahi hai, ye meri  <span style="color:#FF5733;">elder sister</span> ki tarah stand le rahi hai.
    Aur meri zindagi me ye quality rare hai — koi jo bina expect kiye, bina reason, tumhare liye front foot pe aaye.

    Mere dimaag me turant ek thought aaya: Jo mere liye khadi ho… uske khilaf kabhi nahi khada hounga. Wahi pe maine internally decide kar liya — Malik ke saath jo bhi mind games chal rahe the against Karishma, wo ab khatam. Maine apne aap se kasam khayi: Ab Karishma ke against ek bhi galat move nahi hoga. Us din ke baad main ne  <span style="color:#FF5733;">provoke karna band kar diya</span>, Malik ke petty games join karna band kar diya.

    Par problem ye thi ki… jab tak mujhe yeh realization aaya, tab tak  <span style="color:#FF5733;">damage</span> ho chuka tha.
    Peeche maine Malik ke saath milke chhote-mote games kheele the — indirectly roast, facts spread, mind tricks…
    Ye sab perception ka poison ban chuka tha.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap52.jpg", text2, layout="side", image_position="left")





    text3 = """
    <p>
    Malik ki side se main “<span style="color:#FF5733;">bad guy or villain</span>” ban raha tha kyunki main execute karta tha plans, uske saath zyada time rehta tha.
    Wahid ki side pe bhi main “bad guy or villain” ban gaya kyunki Wahid aur Malik ki vibes match nahi hoti thi, aur main Malik ke saath rehta tha.
    “Politics ek zeher hai… jo dheere-dheere character ko khatam karta hai.”
    Aur Wahid… usne apne chhote-chhote seeds plant kar diye the.
    Double politics, <span style="color:#FF5733;">double damage</span>.

    Karishma aur Wahid dheere-dheere close ho rahe the. Karishma Wahid ke baare mein Malik ko batati, Malik mujhe batata.
    Ek din maine Wahid se ek simple sa sawal pucha… aur usne mujhe seedha <span style="color:#FF5733;">jhoot</span> bol diya again and again.

    Mere rules simple the: "Main tumhare liye har situation me ladunga… par mujhe mat play karna, mujhe mat chalna, aur jhoot kabhi mat bolna." Aur Wahid ne wahi kiya jo mujhe sabse zyada hurt karta hai — jhoot.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap53.jpg", text3, layout="side", image_position="right")




    text4 = """
    <p>
    Ab Karishma ki nazar mein main dono taraf se villain ban raha tha.
    Wahid ne fuel daala, Malik ne apni kahani chalayi.
    Main beech mein khada tha… aur har taraf se teer aa rahe the. <span style="color:#FF5733;">Fielding set thi</span>.
    Main kuch bhi karta… main hi galat lagta.

    Us moment pe maine decide kiya ki ab main ye khel nahi khelunga.
    or mujhe wo moment yaad aaya…
    Wo moment jab Karishma ne mere liye stand liya tha.
    Wo ek line… "Tahir ko kuch mat bolna…"

    Ye sirf defence nahi thi… ye ek <span style="color:#FF5733;">debt</span> tha.
    Aur main un logon me se hoon jo debt hamesha chukate hain… chahe uske liye puri game hi kyun na todni pade.

    Main ek din chup raha. Observe karta raha.
    Doosre din maine apne andar ke dark side se baat ki — wo side jo har cheez <span style="color:#FF5733;">cold-blooded</span> tarike se plan karti hai.
    Aur us awaaz ne mujhe kaha: "Agar villain banana hi hai… to normal villain nahi, <span style="color:#FF5733;">nightmare</span> ban jo unki kahani ka hamesha hissa rahe."
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap56.jpg", text4, layout="side", image_position="left")



    text5 = """
    Us din ke baad mujhe kisi ki approval nahi chahiye thi.
    Main hero nahi banna chahta tha… "Main wo banunga jiska naam sunte hi unka heartbeat ruk jaaye." Agar shanti se Karishma ko bachana mushkil hai… to main <span style="color:#FF5733;">toofan banunga</span>.
    <br> <br>
    Har war ko ek grandmaster chahiye.
    Aur agar mujhe <span style="color:#FF5733;">Shakuni Mama</span> banna pade… main banunga. Plan simple tha: Direct attack nahi. Mind games jo unke apne actions ko unke khilaf use kare. Silence as a weapon. Har jung ko ek strategist chahiye. Mind games… jo dikhte simple hain, par tod dete hain foundation.

    <table border="1" cellpadding="8" cellspacing="0" style="width:100%; border-collapse:collapse; text-align:left;">
    <tr>
        <th style="width:50%;">Malik</th>
        <th style="width:50%;">Wahid</th>
    </tr>
    <tr>
        <td>Jhoot bola.</td>
        <td>Jhoot bola.</td>
    </tr>
    <tr>
        <td>Karishma ke saath galat kar raha tha.</td>
        <td>Karishma ko instigate karna.</td>
    </tr>
    <tr>
        <td>Mere saath vishwasghat kiya (will reveal in next chapter).</td>
        <td>6 saal purani dosti pe comment pass karna.</td>
    </tr>
    <tr>
        <td>Karma milega… main deliver karunga.</td>
        <td>Tujhe bhi karma milega… main khud dunga.</td>
    </tr>
    </table>

    """
    create_image_text_layout("attached_assets/generated_images/chap57.jpg", text5, layout="side", image_position="right")







    text6 = """
    <p>
    Log samajhte hain ki loud rehna jeet dilata hai. Galat. "Chup reh ke tum kisi ka dimaag tod sakte ho… bina ek shabd bole."

    Mera plan tha: Malik ko apni galtiyan repeat karne do. Wahid ko apne trap me chalne do. Dono ko apne hi actions me phasne do. <span style="color:#FF5733;">Best revenge?</span> "Enemy ko destroy karna nahi… enemy ko apne aap ko destroy karne dena."

    Aur jab wo din aayega…
    Har VC me sannata chha jayega.
    Har awaaz darr me badal jayegi.
    Aur wo yaad rakhenge — Wo din jab Tahir ne unke saath khelna chhoda… aur unke khilaf khelna shuru kiya.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap58.jpg", text6, layout="side", image_position="left")






    create_image_text_layout("attached_assets/generated_images/chap5ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>The best revenge is never to destroy your enemy with your own hands, but to let them destroy themselves. Karma doesn’t need a weapon, it only needs patience— and I am that patience personified. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 
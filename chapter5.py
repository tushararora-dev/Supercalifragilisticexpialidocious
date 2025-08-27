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
    Par mere liye wo turning point shanti leke nahi aaya… Wo leke aaya ek andheraa toofan — jisme mujhe apna purana roop todna tha… aur ek naya roop banana tha.


    Mujhe yaad hai, sab kuch badla kaise.
    Ek normal sa sham tha. Public VC mein 10-12 log baithe the. Hasna, mazaak, thoda roast, thoda bakwaas — wahi usual scene.
    Aur phir kisi ne mere liye ek teekha sa comment maara.

    Main jawab dene hi wala tha ki ek awaaz aayi ek awaaz chhapi sab awaazon ke upar — strong, clear, protective.
    Karishma:. “Oyee… Tahir ko kuch mat bolna samjhe? @#$& @#$_ kar dungi tumhe!”

    Us moment me ek ajeeb si khamoshi mere andar utar gayi.
    Baat sirf shabdon ki nahi thi… baat thi uske tone ki.
    ye sirf words nahi the… ye ek feel thi.
    Uska tone wo normal friendly tone nahi tha — usme ek protectiveness thi, ek boundary thi jo usne mere liye draw ki.
    Us pal wo server ki ek member nahi thi… wo meri younger sister thi.

    Us pal mujhe laga… ye ladki sirf VC ki ek member nahi hai, ye meri elder sister ki tarah stand le rahi hai.
    Aur meri zindagi me ye quality rare hai — koi jo bina expect kiye, bina reason, tumhare liye front foot pe aaye.

    Mere dimaag me turant ek thought aaya:

    "Jo mere liye khadi ho… uske khilaf kabhi nahi khada hounga."

    Wahi pe maine internally decide kar liya — Malik ke saath jo bhi mind games chal rahe the against Karishma, wo ab khatam.
    Maine apne aap se kasam khayi:

    "Ab Karishma ke against ek bhi galat move nahi hoga."

    Us din ke baad main ne provoke karna band kar diya, Malik ke petty games join karna band kar diya.


    Par problem ye thi ki… jab tak mujhe yeh realization aaya, tab tak damage ho chuka tha.
    Peeche maine Malik ke saath milke chhote-mote games kheele the — indirectly roast, facts spread, mind tricks…
    Ye sab perception ka poison ban chuka tha.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap41.jpg", text1, layout="side", image_position="right")



    text11 = """
    <p>

    Malik ki side pe main “bad guy or villain” ban raha tha kyunki main execute karta tha plans, uske saath zyada time rehta tha.
    Wahid ki side pe bhi main “bad guy or villain” ban gaya kyunki Wahid aur Malik ki vibes match nahi hoti thi, aur main Malik ke saath rehta tha.
        “Politics ek zeher hai… jo dheere-dheere character ko khatam karta hai.”
    Aur Wahid… usne apne chhote-chhote seeds plant kar diye the.
    Double politics, double damage.

    Karishma aur Wahid dheere-dheere close ho rahe the. Karishma Wahid ke baare mein Malik ko batati, Malik mujhe batata.
    Ek din maine Wahid se ek simple sa sawal pucha… aur usne mujhe seedha jhoot bol diya again and again.

    Mere rules simple the:

    "Main tumhare liye har situation me ladunga… par mujhe mat play karna, mujhe mat chalna, aur jhoot kabhi mat bolna."

    Aur Wahid ne wahi kiya jo mujhe sabse zyada hurt karta hai — jhoot.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap42.jpg", text11, layout="side", image_position="left")




    text2 = """
    <p>
    Ab Karishma ki nazar mein main dono taraf se villain ban raha tha.
    Wahid ne fuel daala, Malik ne apni kahani chalayi.
    Main beech mein khada tha… aur har taraf se teer aa rahe the.

    Fielding set thi.
    Main kuch bhi karta… main hi galat lagta.

    Us moment pe maine decide kiya ki ab main ye khel nahi khelunga.
    Par phir mujhe wo moment yaad aaya…
    Wo moment jab Karishma ne mere liye stand liya tha.
    Wo ek line…

    "Tahir ko kuch mat bolna…"

    Ye sirf defence nahi thi… ye ek debt tha.
    Aur main un logon me se hoon jo debt hamesha chukate hain… chahe uske liye puri game hi kyun na todni pade.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap43.jpg", text2, layout="side", image_position="right")



    text3 = """
    Main ek din chup raha. Observe karta raha.
    Doosre din maine apne andar ke dark side se baat ki — wo side jo har cheez cold-blooded tarike se plan karti hai.
    Aur us awaaz ne mujhe kaha:

    "Agar villain banana hi hai… to normal villain nahi, nightmare ban jo unki kahani ka hamesha hissa rahe."

    Us din ke baad mujhe kisi ki approval nahi chahiye thi.
    Main hero nahi banna chahta tha…

    "Main wo banunga jiska naam sunte hi unka heartbeat ruk jaaye."

    Agar shanti se Karishma ko bachana mushkil hai… to main toofan banunga.
    """
    create_image_text_layout("attached_assets/generated_images/chap44.jpg", text3, layout="side", image_position="left")



    text31 = """
    <p>
    Par ek din teeno ka Ashara ke saath clash ho gaya. Baatein abuse tak pahunch gayi. Ashara ko kuch pata nahi chala, par mere andar ek awaaz thi:
    "Karma dena zaroori hai. <span style="color:#FF5733;">Loyalty mere khoon me hai</span>. Agar nahi diya, toh yeh din mere liye daag ban jayega."
    Tab samjha —
    “Loyalty ka matlab hamesha haan me haan milana nahi hota. Kabhi-kabhi sacchai ke liye apne hi dost ke saamne khada hona padta hai.”

    Phir Wahid aur Malik ke beech bonding kharab hone lagi. Dono <span style="color:#FF5733;">impulsive</span> the — bolne se pehle sochte nahi, aur bol diya toh regret bhi nahi. Trigger hone me time nahi lagta tha. Malik aur Karishma ki soch match karti thi, isliye Wahid ko aur problem hone lagi.
    Mere liye situation complex ho gayi:
    <ul>
    <li>Main Karishma ko Wahid se milvane ki koshish kar raha tha.</li>
    <li>Karishma aur Malik ki soch milti thi.</li>
    <li>Wahid aur Malik ki fight ho gayi.</li>
    </ul>
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap45.jpg", text31, layout="side", image_position="right")




    text4 = """
    <p>
    Main bich me fas gaya
    Wahid aur Malik dono mujhe ek doosre ke khilaf bhadkate.
    "Tere saath hoon, uske nahi," dono alag-alag mujhe kehte.
    Aur dono alag VC me baithkar Karishma ko bulane lagte. <span style="color:#FF5733;">Karishma or main confused</span> kiska sath du.

    Pehle Wahid Karishma ke messages ignore karta tha.
    "Mujhe uski soch pasand nahi," woh kehta.
    Lekin dheere-dheere connect karne laga. Shayad insecurity thi — kyunki Malik ke saath Karishma ki bonding strong ho rahi thi.
    Main aur Malik apna game chalate rahe — Karishma ko <span style="color:#FF5733;">ajeeb situations</span> me daal kar reaction check karna.
    Par ek din realise hua — execution ka kaam main hi kar raha hoon… aur main hi phas raha hoon.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap46.jpg", text4, layout="side", image_position="left")



    text5 = """
    Dheere-dheere Karishma aur Malik ki good friend wali bonding ban gayi.
    Aur Karishma aur Wahid ka relationship shuru ho gaya. Wahid ne kaafi effort lagaya — camera on karke baatein, late-night calls…
    Par twist yeh tha — jo bhi baat Karishma Wahid ke saath karti, woh Malik ko bata deti. Kyunki Malik pe uska trust tha.
    Aur Malik mujhe batata, kyunki hum dono ek game khel rhe the.
    Malik ne ek baar mujhe bola —
    "Dekha, kitni easily yeh apne sab secrets de deti hai? Trust karta hai par pata nahi kis hadd tak."
    Main sirf socha — "<span style="color:#FF5733;">Yeh game ab aur dangerous hone wala hai</span>."

    Us waqt maine sirf ek baat sochi —
    “Zindagi me har insaan ek game khel raha hota hai. Bas fark yeh hota hai, kisi ko pata hota hai ki vo game me hai… aur kisi ko bilkul bhi nahi.”
    “<span style="color:#FF5733;">Zindagi ek chessboard hai</span>. Har kisi ka role fix hota hai — king, queen, rook… aur kuch log bas pawn ban jaate hain kyunki unhe pata hi nahi hota ki game chal raha hai.”

    """
    create_image_text_layout("attached_assets/generated_images/chap47.jpg", text5, layout="side", image_position="right")




    create_image_text_layout("attached_assets/generated_images/chap4ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>Friendship is not only about standing beside someone, sometimes it’s about standing for the truth even against them. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 
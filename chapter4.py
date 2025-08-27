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
    create_image_text_layout("attached_assets/generated_images/chap4main.jpg", layout="full")


    text0 = """
    <h2>Chapter 3: When Destiny Chose Four Souls to Meet</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    text1 = """
    <p>
    Kuch log milte nahi, milaye jaate hain. Aur jab <span style="color:#FF5733;">taqdeer</span> chaar raahon ko ek mod pe laati hai… kahani ban jaati hai.  
    Taqdeer ka khel ajeeb hota hai… kabhi log milte hain toh lagta hai bas ek normal mulaqat hai. Lekin saal baad samajh aata hai — woh mulaqat ek kahani ka shuruaat thi.”

    Samay aagya tha.
    Jab hum chaar — main yani Tahir, Malik, Wahid — aur ek nayi mehmaan, Karishma, ek hi kahani ke hissa banne wale the.
    Chapter 3 ke baad, Karishma ka aana ek habit ban gaya. Dheere-dheere woh hamare Discord ke voice channel me aa kar baithne lagi.
    Wahi jagah jahan hamari core team hoti thi,
    jokes hote the, roasting hoti thi, hansi, masti, friendly fights, kabhi full-on online clashes. kabhi heated arguments aur kabhi-kabhi chhoti-moti online fights bhi.

    Usi chill corner me, ek din, <span style="color:#FF5733;">Malik aur Karishma</span> ka aamna-saamna hua or PFP encounter hua. Malik ko pehle se andaza tha ki koi contractor group me hai, par official introduction maine hi karvaya.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap41.jpg", text1, layout="side", image_position="right")



    text11 = """
    <p>


    Main: “Malik, yeh hai Karishma. Contractor wali jo maine bataya tha.”
    Malik (thoda casual tone me): “Hmm… interesting.”

    
    Shuru me bas casual hi tha, par kuch hafton me hi dono ki <span style="color:#FF5733;">bonding</span> shuru ho gayi or dono ki chemistry grow hone lagi. kyunki entertainment me dono ek jaise the ekdam hatke.
    Unke andar sharam naam ki cheez nahi. Bas unapologetic energy. aur limit naam ka concept unke dictionary me exist nahi karta tha. Dono ka attitude ekdum seedha tha — “<span style="color:#FF5733;">I don’t give a f**k</span>.”
    Par Karishma alag thi.


    Real life se kuch insecurities thi, lekin online sharp, fast thinker, tez, aur kabhi-kabhi oversmart. Malik bhi utna hi tez tha, aur oversmart log usse pasand nahi the — bas condition yeh thi ki agar woh entertain kar rahe ho, toh chal jayega.
    Main kabhi-kabhi Malik se sunta — "Isme woh character hai jo main bachpan me tha… lekin ab mujhe yeh <span style="color:#FF5733;">oversmart</span> aur fake cool log bilkul pasand nahi."

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap42.jpg", text11, layout="side", image_position="left")




    text2 = """
    <p>
    Hum teen — main yani Tahir, aur Malik — milkar kabhi logon ko roast karte, kabhi online clashes me masti lete. kabhi random online fights me maza lete. Par parde ke peeche, hum Karishma ke <span style="color:#FF5733;">character analysis</span> kar rahe the.
    Fir shuru hua uska trust test game.
    Karishma kabhi mere through Malik ki loyalty test karti, kabhi Malik ke through mera trust test hota. Par hum dono aapas mein baith kar yeh discuss kar rahe the ki yeh kitni tez chal rahi hai. Isko pata hi nahi ki hum dono ek team mein hain. Malik ke dimaag me plan hota, execution ka kaam mere sar. Situation kuch bhi ho sakti thi —

    <table border="1" cellpadding="5">
    <tr>
        <td>1. Random awkward conversations</td>
        <td>2. Hypothetical moral dilemmas</td>
    </tr>
    <tr>
        <td>3. Sudden group switch test</td>
        <td>4. Trigger traps</td>
    </tr>
    </table>

    Main khud sochta tha —
    "Yeh jo hum kar rahe hain, yeh galat hai… par maza aa raha hai."
    hum uske lia alag-alag situation create karte, jaise weird scenarios, taaki hum dekh saken ki samne wala react kaise karega. 
    Haste-haste din nikal rahe the, par kabhi-kabhi dil me guilt bhi aata tha. Aur ek <span style="color:#FF5733;">personal rule</span> mere dimaag me tha:
    “Jise maine milvaya hai, usko door bhi main hi karunga agar kisi ne betray kiya.”


    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap43.jpg", text2, layout="side", image_position="right")



    text3 = """
    <p>
    Bonding badhti gayi, aur Karishma openly kehne lagi ki usse ek <span style="color:#FF5733;">boyfriend</span> chahiye.
    Maine socha — "Wahid sahi rahega."
    Uske samne maine Wahid ki tarif ki, aur Wahid ke samne Karishma ki.
    Main har psychological trick use karta —
    <ul>
    <li><span style="color:#FF5733;">Reciprocity Principle</span>: ek dusre ke liye chhoti chhoti favours karwana, taaki bonding naturally ho.</li>
    <li><span style="color:#FF5733;">Mirroring</span>: ek dusre ke tone, words copy karna taaki similarity feel ho.</li>
    <li><span style="color:#FF5733;">Social Proof</span>: unke saamne ek dusre ki tareef karna taaki trust build ho.</li>
    </ul>
    <p>
    Mulaqat karvayi <span style="color:#FF5733;">Ashara's server</span> par. Ashara mera 6 saal purana dost tha, aur yeh log usse sirf 4 mahine se jaante the.
    Ab hum chaar ho gaye the — main, Malik, Wahid, aur Karishma.
    Enjoyment ka level double ho gaya. Main har trick try karta ki Wahid aur Karishma ki bonding ban jaye.
    </p>
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
 
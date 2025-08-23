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
        font-size: 16px !important;
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
    create_image_text_layout("attached_assets/generated_images/chap2main.jpg", layout="full")


    text0 = """
    <h2>Chapter 2: Anger Has a Name – Wahid</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <p>Malik ke sath meri baat-chit chal hi rahi thi ki ek aur chehra meri zindagi me aaya – Wahid. Random voice channel me mulaqat hui thi. Pehle to friendly roast, halka-phulka mazaak, aur dheere-dheere lambe sessions tak baat. Wahid ki ek baat alag thi – usne pehli hi mulakaat me meri awaaz pe dhyaan diya.
    "<span style="color:#FF5733;">Tere voice me power hai</span>, bro… log sunte hi ruk jate hain."
    Woh baar-baar meri tarif karta. Kabhi mujhe phone pe bulata, kabhi mujhe naye logo ke beech le jaata, sirf isliye ki unhe impress kar sake:
    "Yeh mere sath hai, sun na, iski voice me alag hi power hai."
    <br> <br>
    Pehle mujhe lagta woh bas ek casual dost hai, lekin dheere-dheere maine dekha ki Wahid apni taraf se rishte ko aage badhane ki koshish kar raha tha. Maine socha, agar banda khud haath badha raha hai, toh main bhi peeche kyu rahun? Aur fir main uski fights me shaamil hone laga, uski madad karne laga… aur kabhi-kabhi sirf entertainment ke liye bhi uska saath dene laga.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap22.jpg", text1, layout="side", image_position="right")



    text2 = """
    <p>
    Ek raat VC pe casual mood tha. Wahid chill kar raha tha, jokes crack kar raha tha. Suddenly ek ladke ne usse interrupt kiya:
    Random Guy: “Bhai, chill kar na. Overacting mat kar.”
    Aur ek pal me Wahid ka mask tod gaya.
    Wahid (chillate hue):
    “Overacting? <span style="color:#FF5733;">Oye @#$%^&*!</span> Tujhe pata bhi hai tu kis se baat kar raha hai? Main wahid hoon – jahan main baitha na, wahan log khade hote hain.” Room silent ho gaya. Mujhe samajh aa gaya – yeh banda <span style="color:#FF5733;">ego ka prisoner</span> hai.
    </p>
    """
    create_image_text_layout(text_content=text2, layout="full")



    text3 = """
    <p>Wahid: A Torn Personality, Wahid ke sath bonding aisi bani ki main sochne laga, “Isko to main Malik se bhi milvauga.” Lekin usse pehle mujhe khud samajhna tha ki yeh banda aakhir hai kaisa. Wahid ek contradiction tha, ek taraf dosti, doosri taraf gussa. </p>
    <ul>
        <li><strong>Dil toota aashiq</strong> – ex ne dhoka diya tha, aur us dard ka bojh uske har lafz me tha.</li>
        <li><strong>Hard ego wala</strong> – chhoti si baat pe bhi blast.</li>
        <li><strong>Public VC ka purana khiladi</strong> – har baat ko style me rakhna aata tha.</li>
        <li><strong>Ladki-bazzi</strong> – 6-7 breakups, patchups, sympathy drama, aur jhuta pyaar ka khel.</li>
        <li><strong>Leak Hub ka operator</strong> – online ki dark duniya se bhi uska lena dena tha: raiding, server bombing, leaks.</li>
        <li><strong>Double nature</strong> – ladko ke samne ek alag chehra, ladkiyon ke samne ek aur.</li>
        <li><strong><span style="color:#FF5733;">Comedian</span></strong> – jab mood ban jaye toh zabardast comedy bhi karta.</li>
    </ul> </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap23.jpg", text3, layout="side", image_position="left")


    text4 = """

    <p>Ek taraf sweet banda lagta tha, doosri taraf shaitaan. Pehle mujhe laga yeh bas ek casual dost hai, lekin dheere-dheere uski presence heavy lagne lagi. Mujhe mehsoos hua – yeh banda ek walking conflict hai.
    <table>
    <tr>
        <td>Dosti bhi karta tha… aur dusre pal ego se blast bhi kar deta.</td>
        <td>Kabhi dil se vulnerable lagta, kabhi dark world ka operator.</td>
        <td>Kabhi sweet Punjabi banda, kabhi lava ka pahad.</td>
    </tr>
    </table>
    """
    create_image_text_layout(text_content=text4, layout="full")


    text5 = """
    <p>
    Mujhe uski ek <span style="color:#FF5733;">psychological weakness</span> samajh aa gayi – uska ego.
    Uska gussa trigger hota tha jaise hi uski izzat ko chot lagti.
    Ek baar maine deliberately usse ek debate me uljha diya. Usne chillana shuru kiya, lekin main calm raha. Fir usi calmness me maine usse samjhaya:
    <br><br>
    Me (calm tone): “Bhai, tu gusse me jo bolta hai na, usse teri baat ki value khatam ho jaati hai. Tere paas ek aur shakti hai – teri awaaz. Power gusse me nahi, authority me hai.”
    Wahid ruk gaya. Uski aankhon me jwala thi, par us jwala ke peeche ek thought spark hua.
    Mujhe pata tha – maine uske mind me ek <span style="color:#FF5733;">psychological hook</span>  daal diya hai. Yehi ego redirection technique hai – banda jab apne hi weapon (awaaz) ka positive angle sunta hai, toh apna gussa digest kar leta hai.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap24.jpg", text5, layout="side", image_position="right")



    text6 = """
    <p>
    Wahid ka Dard : 
    Ek raat usne apni ex ki kahani sunai. Pehle toh uska usual macho tone tha, lekin dheere-dheere uski awaaz toot gayi.
    Wahid (rote hue):
    “Usne mujhe cheat kiya… Maine abuse kiya uska… aur main phir bhi usse pyaar kehta raha. Kya main bewakoof tha?”
    Us moment me maine ek cheez notice ki – uska gussa asal me ek mask tha. Andar ek wounded lover, <span style="color:#FF5733;">ek broken man</span>  chhupa tha.
    Maine socha – agar banda apni ladki me maa ka chehra nahi dekh paata, toh woh pyaar nahi, addiction hai.
    Lekin main chup raha. Bas suna.

    Mera apna funda simple tha – <span style="color:#FF5733;">loyalty ke badle loyalty</span> .
    Agar tum mere liye sahi ho, main duniya se lad jaunga. Lekin agar tumne jhooth bola, ya dhokha diya, toh main bhi wahi game khelunga – aur woh aisi game hoti jo dusre ke dimaag me stress aur dard chhod jaati. Aur mujhe lagta tha kismat ne mujhe uske samne laaya hi isliye hai – ya toh use theek karne ke liye, ya phir use samjhane ke liye.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap26.jpg", text6, layout="side", image_position="left")



    text7 = """
    <p>
    Usne mujhe online ki kuch andheri duniya dikhayi – raiding servers, leaks hub, bomber groups.
    Mujhe pehle woh sab funny laga, fir disgusting. Uske liye yeh ek game tha, mere liye ek darawna truth. Usne ek din casually bola: “Mere dost ka server hai matlab mera server hai.”
    Mujhe samajh aa gaya – yeh banda sirf entertainment ke liye jeeta hai. Koi permanent dosti, koi permanent rishta uske liye nahi hai. yeh banda stability ke liye nahi bana. Iske liye dosti bhi ek entertainment package hai.
    </p>
    """
    create_image_text_layout(text_content=text7, layout="full")





    text8 = """
    <p>
    Pehli baar laga ki yeh ek <span style="color:#FF5733;">sweet Punjabi</span> banda hai. Lekin jaise-jaise waqt guzra, maine uska asli rang dekha – chhoti si baat pe gussa, phir usi speed se shaant bhi, ladayi me top aur backchodi me perfect. Ek taraf laughter, doosri taraf lava. Wahid ek aisa insaan tha jisme anger ka naam likha tha – Anger Has a Name: Wahid. <br> <br>
    Ek pal woh comedy king tha – jokes, laughter, full Punjabi energy. Doosre pal woh lava tha – chhoti-si baat pe dhamaka.
    Ek baar VC pe usne mujhe tease kiya: Wahid: “Bro, tu Malik ke sath jyada time deta hai. Main secondary lagta hoon kya?”
    Maine calm reply diya: “Secondary tu kabhi tha hi nahi. Bas samajh le, tu ek aur story hai jo mujhe likhni hai.”
    Woh hansa… lekin us hansne ke peeche  <span style="color:#FF5733;">jealousy aur insecurity</span> dono the.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap27.jpg", text8, layout="side", image_position="right")




    text9 = """
    <p>Mujhe ek cheez samajh aayi:
    <ul>
    <li>Gussa ek shield hai, jo broken insaan apne dard ko chhupane ke liye pehenta hai.</li>
    <li>Backchodi ek mask hai, jisse banda apni tanhayi ko cover karta hai.</li>
    <li>Loyalty ek trap hai – agar tum ek insaan ko genuinely loyal feel kara do, woh tumse kabhi door nahi hoga.</li>
    </ul>
    </p>
    <p>
    Wahid meri zindagi me ek paradox tha – ek aisa insaan jisme dosti bhi thi, andhera bhi, comedy bhi aur lava bhi. Aur ek pal mujhe laga – Kismat hi hoti hai jo hume aise logon se milwati hai. Shayad main Wahid ke liye ek mirror tha – jo uske gusse, uske dard aur uski ego ka asli chehra dikha raha tha. Aur shayad Wahid mere liye ek test tha – ki main apni loyalty kitni door tak nibha sakta hoon.
    Anger had a face.
    Anger had a voice.
    <span style="color:#FF5733;">Anger had a name – Wahid</span>.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap29.jpg", text9, layout="side", image_position="left")

    create_image_text_layout("attached_assets/generated_images/chap2ban.png", layout="full")
    text10 = """
    <p> <div class='beth1'>“Emotion is fuel, character is the engine. Anger is just energy — guide it like a river with banks. Without banks, it floods and destroys; with them, it powers your purpose and moves you forward." - Danjin Master <br> <br>
    </p>

    """
    create_image_text_layout(text_content=text10, layout="full")
 
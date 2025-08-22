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
        border: 1px solid #444;
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
    create_image_text_layout("attached_assets/generated_images/chap2.png", layout="full")


    text0 = """
    <h2>Chapter 2: Anger Has a Name – Wahid</h2>
    <p>A new chapter will come out every Wednesday...... </p>
    """
    create_image_text_layout(text_content=text0, layout="full")

#     text1 = """
#     <p>Malik ke sath meri baat-chit chal hi rahi thi ki ek aur chehra meri zindagi me aaya – Wahid. Random voice channel me mulaqat hui thi. Pehle to friendly roast, halka-phulka mazaak, aur dheere-dheere lambe sessions tak baat. Wahid ki ek baat alag thi – usne pehli hi mulakaat me meri awaaz pe dhyaan diya.

# "Tere voice me power hai, bro… log sunte hi ruk jate hain."

# Woh baar-baar meri tarif karta. Kabhi mujhe phone pe bulata, kabhi mujhe naye logo ke beech le jaata, sirf isliye ki unhe impress kar sake:
# "Yeh mere sath hai, sun na, iski voice me alag hi power hai."

# Pehle mujhe lagta woh bas ek casual dost hai, lekin dheere-dheere maine dekha ki Wahid apni taraf se rishte ko aage badhane ki koshish kar raha tha. Maine socha, agar banda khud haath badha raha hai, toh main bhi peeche kyu rahun? Aur fir main uski fights me shaamil hone laga, uski madad karne laga… aur kabhi-kabhi sirf entertainment ke liye bhi uska saath dene laga.

# Psychology Trick: “The Ego Trap”

# Maine dekha, Wahid ko sabse zyada trigger karta tha uska ego. Jab koi usse oppose karta, ya uski izzat ko chhoti si chot bhi lagti, toh woh explode kar jata.

# Ek baar maine deliberately usse ek debate me uljha diya. Usne chillana shuru kiya, lekin main calm raha. Fir usi calmness me maine usse samjhaya:
# "Tu gusse me jo bolta hai, usse teri baat ki value khatam ho jati hai. Power tere gusse me nahi, teri awaaz ki authority me hai."

# Woh chup ho gaya. Yehi ego redirection technique hai – banda jab apne hi weapon (awaaz) ka positive angle sunta hai, toh apna gussa digest kar leta hai.

# Wahid ka Dard

# Ek raat usne apni ex ki kahani batayi. Rote hue bola:
# "Usne mujhe cheat kiya… abuse bhi kiya… fir bhi main sochta tha yeh pyaar hai."

# Main sunta raha, lekin andar hi andar mujhe laga – agar tum ladki ko gaali dete ho, usme maa ko nahi dekhte, toh wo pyaar kaisa? Maine use samjhaya bhi, lekin mujhe samajh aa raha tha ki uska dard asli tha, sirf nakli drama nahi.

# Mere Rules

# Mera apna funda simple tha – loyalty ke badle loyalty.
# Agar tum mere liye sahi ho, main duniya se lad jaunga. Lekin agar tumne jhooth bola, ya dhokha diya, toh main bhi wahi game khelunga – aur woh aisi game hoti jo dusre ke dimaag me stress aur dard chhod jaati.

# Wahid ko maine ye clearly samjha diya tha. Aur mujhe lagta tha kismat ne mujhe uske samne laaya hi isliye hai – ya toh use theek karne ke liye, ya phir use samjhane ke liye.

# Wahid’s Dark World

# Usne mujhe online ki kuch andheri duniya dikhayi – raiding servers, leaks, bomber groups.
# Mujhe pehle woh sab funny laga, fir disgusting. Uske liye yeh ek game tha, mere liye ek darawna truth.

# Usne ek din casually bola:
# "Mere dost ka server hai matlab mera server hai. Jo main chaahun wahi hoga."

# Maine samjha – yeh banda sirf entertainment ke liye jeeta hai. Koi permanent dosti, koi permanent rishta uske liye nahi hai.

# The Explosive Nature

# Pehli baar laga ki yeh ek sweet Punjabi banda hai. Lekin jaise-jaise waqt guzra, maine uska asli rang dekha –

# chhoti si baat pe gussa,

# phir usi speed se shaant bhi,

# ladayi me top,

# aur backchodi me perfect.

# Ek taraf laughter, doosri taraf lava. Wahid ek aisa insaan tha jisme anger ka naam likha tha – Anger Has a Name: Wahid.

# The Psychological Takeaway

# Wahid ne mujhe ek cheez sikha di:

# Gussa un logon ka shield hota hai jo andar se toot chuke hote hain.

# Backchodi ek mask hai, jisse banda apne dard ko chhupata hai.

# Aur loyalty ek psychological hook hai – agar tum ek bande ko genuinely loyal feel karwa do, toh woh tumse kabhi alag nahi hoga.

# End Note

# Kismat hi hoti hai jo hume aise logon se milwati hai. Shayad main Wahid ke liye ek mirror tha – jo uske gusse, uske dard aur uski ego ka asli chehra dikha raha tha.
# Aur shayad Wahid mere liye ek test tha – ki main apni loyalty kitni door tak nibha sakta hoon.
#     </p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap22.png", text1, layout="side", image_position="left")

 


#     text4 = """
#     <p>Wahid: A Torn Personality : Wahid ke sath bonding aisi bani ki main sochne laga, “Isko to main Malik se bhi milvauga.” Lekin usse pehle mujhe khud samajhna tha ki yeh banda aakhir hai kaisa. Wahid ek contradiction tha – ek taraf dosti; doosri taraf gussa, ego aur hamesha ladayi ke mood me.
#     <ul>
#         <li><strong>Dil toota aashiq</strong> – ex ne dhoka diya tha, aur us dard ka bojh uske har lafz me tha.</li>
#         <li><strong>Hard ego wala</strong> – chhoti si baat pe bhi blast.</li>
#         <li><strong>Public VC ka purana khiladi</strong> – har baat ko style me rakhna aata tha.</li>
#         <li><strong>Ladki-bazzi</strong> – 6-7 breakups, patchups, sympathy drama, aur jhuta pyaar ka khel.</li>
#         <li><strong>Leak Hub ka operator</strong> – online ki dark duniya se bhi uska lena dena tha: raiding, server bombing, leaks.</li>
#         <li><strong>Double nature</strong> – ladko ke samne ek alag chehra, ladkiyon ke samne ek aur.</li>
#         <li><strong>Comedian</strong> – jab mood ban jaye toh zabardast comedy bhi karta.</li>
#     </ul>
#     <p>Ek taraf sweet banda lagta tha, doosri taraf shaitaan. Pehle mujhe laga yeh bas ek casual dost hai, lekin dheere-dheere uski presence heavy lagne lagi.
#     <ul>
#     <li>Dosti bhi karta tha… aur dusre pal ego se blast bhi kar deta.</li>
#     <li>Kabhi dil se vulnerable lagta, kabhi dark world ka operator.</li>
#     <li>Kabhi sweet Punjabi banda, kabhi lava ka pahad.</li>
#     </ul><p>Mujhe mehsoos hua – yeh banda ek walking conflict hai.<p>
#     """
#     create_image_text_layout("attached_assets/generated_images/chap22.png", text4, layout="side", image_position="right")


    # text5 = """
    # <p>
    # The Ego Trap: Maine dekha, Wahid ko sabse zyada trigger karta tha uska ego. Jab koi usse oppose karta, ya uski izzat ko chhoti si chot bhi lagti, toh woh explode kar jata.

    # Ek baar maine deliberately usse ek debate me uljha diya. Usne chillana shuru kiya, lekin main calm raha. Fir usi calmness me maine usse samjhaya:
    # "Tu gusse me jo bolta hai, usse teri baat ki value khatam ho jati hai. Power tere gusse me nahi, teri awaaz ki authority me hai."

    # Woh chup ho gaya. Yehi ego redirection technique hai – banda jab apne hi weapon (awaaz) ka positive angle sunta hai, toh apna gussa digest kar leta hai. </p>
    # """
    # create_image_text_layout("attached_assets/generated_images/chap22.png", text5, layout="side", image_position="left")

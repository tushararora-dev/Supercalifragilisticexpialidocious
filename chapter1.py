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
    create_image_text_layout("attached_assets/generated_images/chap1.jpg", layout="full")


    text0 = """
    <h2>Chapter 1: When Tahir Found Malik, Chaos Found Me</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")

    text1 = """
    <p>Aaj jab main apni kahani likhne baitha hoon, to sabse pehla sawal mere dimag mein ghoom raha hai – “Akhir main Malik se mila hi kyun?”
    Aur jab mila… to meri zindagi ne ek naya rang le liya.
    Meri aur Malik ki mulaqat kisi reality show ki tarah stage par nahi hui thi. Hum dono ek <span style="color:#FF5733;">Random Discord voice chat</span> mein takraaye the – ek aisi jagah jahan log masti, mazaak, aur thodi si pagalpan bhari backchodi karne aate the. Shayad duniya isse waste of time kehti, lekin mere liye wahi ek nayi duniya thi. Pehle hi din vibe match ho gayi. Reason simple tha: Hum dono coder the. Hum dono Delhi ke the. Aur sabse badi baat – hum dono backchod the.

    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap11.jpg", text1, layout="side", image_position="left")

 
    text2 = """
    <p>
    Main, yani Tahir, ek emotional aur simple insaan tha. Coding karta tha, par dil ke mamle mein zyada sensitive tha. Care karta tha, attachment jaldi ban jati thi, dusro ke liye sacrifice karne ka junoon tha. Creativity meri taaqat thi, aur insaaniyat meri pehchaan.
    Aur saamne tha Malik. 
    Uska dimaag tez tha, aankhon mein ego tha, aur attitude me ek alag hi spark. Use oversmart log bilkul pasand nahi the, aur jo bekaar gyaan baatein karte rehte the na, unhe to ek hi jhatke mein cut kar deta tha. Malik mein ek cheez thi jo mujhse alag thi – usme humanity ki kami thi. Uska funda simple tha: <span style="color:#FF5733;">“I don’t give a f**k”</span>.<br> Ek taraf main tha jo insaan ko sambhalna chahta tha, doosri taraf Malik tha jo insaan ko parakhna chahta tha. Aur jab dono mile, to ek explosive jodi bani – <span style="color:#FF5733;">Creativity met Cleverness</span>. Dheere-dheere humne ek dusre se seekhna shuru kiya.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap12.jpg", text2, layout="side", image_position="right")


    text3 = """
    <ul>
    <li>Main emotional tha, par Malik ne mujhe sikhaya ki emotions ka istemal weapon ki tarah bhi kiya ja sakta hai.</li>
    <li>Main creative tha, aur Malik ne dikhaya ki creativity ko sahi jagah pe thoda galat tareeke se use karne ka maza alag hi hai.</li>
    <li>Humne seekha ki kaise logon ki insecurity aur weakness samajhkar unhe pehle heal karna hai… aur phir unse paise nikalwane hain. (Haan, humne ye kiya. Aur ye galat bhi tha… par us process ka thrill hi alag tha.)</li>
    </ul>
    <p>
    Phir hum dono ne Discord ke duniya mein ek gang banaya – <span style="color:#FF5733;">Anti Bihari</span>.
    Naam ajeeb tha, par uske peeche ek hi motive tha – “Legacy create karni hai. Naam banana hai.” Aur humne banaya bhi. Kai public servers mein humari dhoom machti thi. Hamari team ek tarah ki “mini-mafia” thi, jahan 15-20 log hamesha active rehte the. Lekin us bheed mein bhi asli core sirf hum do hi the – Tahir aur Malik.
    </p>
    """
    create_image_text_layout(text_content=text3, layout="full")

    text4 = """
    <p>Humara daily routine kuch aisa hota tha: Kisi ko roast karna - Moderator se panga lena - Online jail, yaani “Daily Verdict” mein phase rehna - Moderator ko manipulate karke bahar nikalna. Aur phir dobara wahi cycle shuru. Ye ek khel ban gaya tha – <span style="color:#FF5733;">Roast → Punishment → Escape</span>. Aur us khel ka maza hi alag tha. Par ye sirf shuruat thi. Team aur manipulation ke kaam itne complex ho gaye:
    <ul>
    <li>Apni team members ko bachate the har tricky situation me.</li>
    <li>Opponents ko apni party me late — pehle roast, fir izzat, loyalty 10x.</li>
    <li>Ek dusre se ladte bhi the, dikhawa aur real tension dono.</li>
    <li>Small groups ko merge karvake powerful alliance banate.</li>
    <li>Dusre groups se ladai bhi hoti — aur wahan se bhi power aur respect extract karte.</li>
    </ul><p>Ye sab Kalyug ke andar ka game tha — har move calculated, har rishta ek strategy, har emotion weapon. Sirf masti hi nahi, hum coding aur padhaai ki baatein bhi karte the.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap13.jpg", text4, layout="side", image_position="left")

    text5 = """
    <p>Soundboards, equalizers, OBS – sab tools istemal karte the apne opponents ko irritate karne ke liye. Aur haan, hum acche kaam bhi karte the – jaise kisi ko uski problem se nikalna, sahi galat samjhana, ya kisi se sorry bulwana. Lekin phir bhi… accha aur bura, dono ek saath chal raha tha. <br> <br> Main aur Malik dono ke roles clear the: Malik roast karta, main us bande ko sympathy deta. Malik manipulations karta, main banda apni side laata. Malik attack karta, main heal karta. Aur is tarah ek poora cycle chalta rehta. Malik ka ek hi funda tha:
    <ul>
    <li><strong><span style="color:#FF5733;">Pehla step:</span></strong> unke paas jao, unke close bano.</li>
    <li><strong><span style="color:#FF5733;">Doosra step:</span></strong> unki kahaniyon se apne aap ko relate karo. “Haan yaar, main bhi aisa hi feel karta hoon” – bas, connection ban gaya.</li>
    <li><strong><span style="color:#FF5733;">Teesra step:</span></strong> Roz unke dimag me ek hi cheez ghusaate raho, chahe jhoot hi kyon na ho. Aur dheere-dheere woh jhoot bhi unke liye sach ban jaata hai.</li>
    </ul>
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap14.jpg", text5, layout="side", image_position="right")



    text6 = """
    <p>Aur wahi din tha, jab maine samajh liya – dosti, rishton, ya bharose ke piche ek aur game chalta hai. Ek hidden game. Aur main us game ka hissa ban chuka tha. Lekin jo sabse interesting tha, wo tha mera apna tareeka. Malik sharp tha, par main <span style="color:#FF5733;">Chanakya Niti</span> apne style me chalata tha. Saam, Daam, Dand, Bhed. baat nikalwane ke 4 tareeke:
    <ol>
    <li><strong><span style="color:#FF5733;">Saam</span></strong> – Samajhdaari aur buddhi se, samajhkar aur thodi chalaki se baat nikalwana.</li>
    <li><strong><span style="color:#FF5733;">Daam</span></strong> – Kuch badle mein dene ya lene ka vaada karke, yaani kuch exchange karke baat nikalwana.</li>
    <li><strong><span style="color:#FF5733;">Dand</span></strong> – Dand ya punishment dekar, ya kisi ko darr dikhakar baat nikalwana.</li>
    <li><strong><span style="color:#FF5733;">Bhed</span></strong> – Kisi ki kamzori ka fayda utha kar, exploitation karke baat nikalwana.</li>
    </ol><p>Logo ke dimaag ka gate todne ke liye mere paas apne hi sawal the:
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap15.jpg", text6, layout="side", image_position="left")


    text7 = """
    <p>
    <table border="1" cellspacing="0" cellpadding="8" style="border-collapse: collapse; width: 100%;">
        <tr>
            <td>Kya galti hai jo past me jakar theek karna chahoge agar chance mile to?</td>
            <td>Kuch regret hai jo abhi tak chubhta hai?</td>
            <td>Apni life ka sabse accha aur sabse bekar din kaunsa tha?</td>
        </tr>
        <tr>
            <td>Aisi ek cheez jo tum secretly try karna chahte ho?</td>
            <td>Agar koi rules na hote to tumhara perfect day kaisa hota?</td>
            <td>Zindagi ne sabse tough lesson kya sikhaya tumhe?</td>
        </tr>
        <tr>
            <td>Aisi kaunsi baat hai jo tum chahte ho log tumhare baare me samjhe?</td>
            <td>Agar hum teleport kar sakte, to tum kaha jana chahoge?</td>
            <td>Agar tumhe kisi bhi cheez ka darr na ho, to kya karoge?</td>
        </tr>
        <tr>
            <td>Apni zindagi me ek cheez badalne ka chance mile to kya badaloge?</td>
            <td>Sabse pehle toot jao to sabse pehle kiske baare me sochte ho?</td>
            <td>Agar tumhe future me apne aap se milne ka mauka mile, to sabse pehle kya puchoge?</td>
        </tr>
        <tr>
            <td>Tumhari sabse badi strength aur weakness kya hai?</td>
            <td>Agar tum ek superpower le sakte, to kaunsi hoti?</td>
            <td>Tumhare life ka sabse proud moment kaunsa tha?</td>
        </tr>
        <tr>
            <td>Aisa kaunsa sapna hai jo tum abhi tak poora nahi kar paaye?</td>
            <td>Agar tum ek din ke liye kisi aur ki zindagi jee sakte, to kiski hoti?</td>
            <td>Apna sabse bura decision konsa maante ho?</td>
        </tr>
        <tr>
            <td>Tumhe sabse zyada motivate kaun karta hai?</td>
            <td>Agar kal duniya khatam hone wali ho, to tum aaj kya karoge?</td>
            <td>......  Many More</td>
        </tr>
    </table>


    </p>
    """
    create_image_text_layout(text_content=text7, layout="full")




    text8 = """
    <p>
    Ye sawal sirf sawaal nahi the, ye <span style="color:#FF5733;">psychological keys</span> the.
    Inke jawab se log apna sabse hidden side reveal kar dete the. Log mujhe apna "enemy" samajhkar shuru karte the, aur khatam hote-hote apna dost tak ka safar start hojata hai.
    Mera ek aur golden trick tha jo hamesha kaam karta:
    <ol>
    <li>Pehle roast karo — saamne wale ko tod do, uski ego hilao.</li>
    <li>Phir respect do — jahan usne expect nahi kiya, wahan use izzat do.</li>
    <li>Aur uske baad — <span style="color:#FF5733;">Loyalty 2x</span> ho jati thi.</li>
    </ol> <p>Dheere-dheere, humari soch evolve hone lagi.  Uske baaad me samaj gya, how we can do it. jaise logon se past ke regrets, unke dreams, ya unke sabse dark secrets nikalna. Har question ek talwar tha, jo saamne wale ko tod bhi sakta tha, aur bana bhi sakta tha.
    Mujhe lagta tha ki hum dono milke ek aisi machine ban gaye the jo kisi bhi situation me adapt ho sakti thi. Chahe opponent ho, moderator ho, ya koi naya banda – koi tik nahi paata tha.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap16.jpg", text8, layout="side", image_position="right")



    text9 = """
    <p> 
    Aur is sab ke beech… mujhe ehsaas ho raha tha ki meri duniya badal rahi hai.
    Main jo pehle sirf ek simple aur emotional ladka tha, ab main ek aisa insaan ban raha tha jo emotions ko weapon ki tarah istemal karna seekh gaya tha. Malik ne mujhe badal diya tha.
    Aur us din mujhe samajh aaya… <span style="color:#FF5733;">When I found Malik, chaos found me</span>.
    Aur sabse badi baat — story ka naam <span style="color:#FF5733;">Supercalifragilisticexpialidocious</span> ka reference abhi suspense me hai, jo last chapter me khulega.
    </p>
    """
    create_image_text_layout(text_content=text9, layout="full")

    create_image_text_layout("attached_assets/generated_images/chap1ban.jpg", layout="full")
    text10 = """
    <p> <div class='beth1'>“Every meeting in life is written by destiny. And when chaos enters, do not fear — it is not here to end you, but to shape you into who you are meant to be." - Danjin Master <br> <br>
    </p>

    """
    create_image_text_layout(text_content=text10, layout="full")
 

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family: Arial, sans-serif;
}

body{
    background:#111;
    color:white;
}

header{
    background:#000;
    padding:15px;
    border-bottom:2px solid red;
}

nav{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.logo{
    color:red;
    font-size:28px;
    font-weight:bold;
}

nav ul{
    list-style:none;
    display:flex;
}

nav ul li{
    margin-left:20px;
}

nav ul li a{
    color:white;
    text-decoration:none;
    transition:0.3s;
}

nav ul li a:hover{
    color:red;
}

.hero{
    text-align:center;
    padding:100px 20px;
    background:linear-gradient(rgba(0,0,0,0.8), rgba(255,0,0,0.2));
}

.hero h1{
    font-size:50px;
    color:red;
}

.hero p{
    margin-top:15px;
    font-size:20px;
}

.btn{
    display:inline-block;
    margin-top:20px;
    padding:12px 25px;
    background:red;
    color:white;
    text-decoration:none;
    border-radius:5px;
}

.section{
    padding:50px 20px;
    text-align:center;
}

.cards{
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:20px;
    margin-top:20px;
}

.card{
    background:#1a1a1a;
    padding:20px;
    width:280px;
    border:1px solid red;
    border-radius:10px;
    transition:0.3s;
}

.card:hover{
    transform:translateY(-8px);
    box-shadow:0 0 15px red;
}

footer{
    background:black;
    text-align:center;
    padding:20px;
    margin-top:40px;
    border-top:2px solid red;
}

form{
    max-width:500px;
    margin:auto;
}

input, textarea{
    width:100%;
    padding:12px;
    margin:10px 0;
    background:#222;
    color:white;
    border:1px solid red;
}

button{
    padding:12px 20px;
    background:red;
    color:white;
    border:none;
    cursor:pointer;
}
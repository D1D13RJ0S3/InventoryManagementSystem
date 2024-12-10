<!--
Component: AboutUs.svelte
Description: This component displays an "About Us" section with cards for each team member.
It showcases individual profiles with names, roles, icons, and descriptions.
Properties:
  - None
Internal Variables:
  - None
Main Functions:
  - None
External Dependencies:
  - Images for each team member and the company logo.
  - SVG icons used within the profiles.
-->

<div class="cards-container">
  <div class="card">
    <div class="blob"></div>
    <span class="img img-jesus"></span>
    <h2>Jesus<br /><span>Mora</span></h2>
    <h3>Scrum<br /><span>Master</span></h3>
    <p>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M962.267429 233.179429q..."></path>
      </svg>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M123.52064 667.99143l344.526782..."></path>
      </svg>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M950.930286 512q0 143.433143..."></path>
      </svg>
    </p>
    <!-- Text container that appears on the white part -->
    <div class="text-overlay">
      <p>
        Soy alguien que disfruta de la tecnología y la 
        información, apasionado en el buen trabajo
          en equipo y en los sistemas para llevar nuestra imaginación
           a un nivel digital.
      </p>
    </div> 
  </div>

  <div class="card">
    <div class="blob"></div>
    <span class="img img-david"></span>
    <h2>David<br /><span>Perez</span></h2>
    <h3>Development<br /><span>Team</span></h3>
    <p>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M962.267429 233.179429q..."></path>
      </svg>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M123.52064 667.99143l344.526782..."></path>
      </svg>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M950.930286 512q0 143.433143..."></path>
      </svg>
    </p>
    <div class="text-overlay">
      <p>
        Soy un programador entusiasta por conocer mas sobre este mundo, 
        buscando nuevas adversidades para superar y adaptándome a ellas,
         "Alone in the code, together in innovation."
      </p>
    </div> 
  </div>

  <div class="card">
    <div class="blob"></div>
    <span class="img img-didier"></span>
    <h2>Didier<br /><span>Parodis</span></h2>
    <h3>Product<br /><span>Owner</span></h3>
    <p>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M962.267429 233.179429q..."></path>
      </svg>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M123.52064 667.99143l344.526782..."></path>
      </svg>
      <svg class="icon" viewBox="0 0 1024 1024" width="35" height="35">
        <path fill="#f0f0f0" d="M950.930286 512q0 143.433143..."></path>
      </svg>
    </p>
    <div class="text-overlay">
      <p>
        Desarrollador backend con sólida experiencia 
        en la construcción de sistemas eficientes y escalables.
         Aplico mi pasión por la tecnología para optimizar bases de datos y APIs,
          garantizando un producto de alta calidad.
      </p>
    </div> 
  </div>
  <!-- Section at the bottom of the page for the logo and slogan -->
  <div class="footer-page">
    <img src="/assets/img/logo.svg"  alt="Company Logo" class="footer-logo" style="width: 1080px; height: 200px;" />
    <p class="footer-slogan"></p>
  </div>
</div>

<style>
  .cards-container {
    display: flex;
    justify-content: space-between;
    gap: 30px;  
    flex-wrap: wrap;  
    padding: 20px;  
  }

  .card {
    width: 280px;  
    height: 380px; 
    background: #f0f0f0;
    border-radius: 10px;
    text-align: center;
    transition: all 0.5s;
    position: relative;
    margin: 20px;
  }

  .card:hover {
    box-shadow: 0 0 20px 1px rgba(0, 0, 0, 0.623);
    background-color: #4bb8ff;
  }

  .card .blob {
    height: 10px;
    width: 75%;
    border-radius: 0 0 30px 30px;
    margin: 0 auto;
    background-color: #4bb8ff; 
    visibility: visible;
    transition: all 0.3s;
  }

  .card:hover .blob {
    height: 0;
  }

  .card .img {
    display: flex;
    margin: 30px auto 10px auto;
    width: 120px; 
    height: 120px; 
    border-radius: 50%;
    font-size: 15px; 
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0; 
    background-size: cover; 
    background-position: center;
    transition: all 0.5s, opacity 0.5s; 
  }
  .card .img-jesus {
    background-image: url('/assets/img/JesusPic.jpg');
  }

  .card .img-david {
    background-image: url('/assets/img/DavidPic.jpg');
  }

  .card .img-didier {
    background-image: url('/assets/img/DidierPic.jpg');
  }

  .card:hover .img {
    width: 100%;
    height: 70%;
    border-radius: 10px 0 0;
    margin: 0 auto;
    background-color: #f0f0f0;
    z-index: 99999;
    opacity: 0; 
    transition: all 0.5s, opacity 0.5s; 
  }

  .card h2 {
    padding: 15px 10px;
    font-size: 28px; 
    transition: all 0.1s;
    z-index: -99;
    line-height: 20px; 
  }

  .card span {
    font-size: 20px; 
  }

  .card h3 {
    font-size: 22px; 
    color: #000000;
    margin: 10px 0;
    font-weight: normal;
  }

  .card:hover h2 {
    opacity: 0;
    width: 100%;
    position: absolute;
    transition: all 0.5s;
  }

  .card > p {
    opacity: 0;
    transition: all 0.75s;
  }

  .card > p > svg {
    padding: 5px;
  }

  .card:hover > p {
    position: absolute;
    bottom: 15px;
    left: 35px;
    opacity: 1;
    transition: all 0.1s;
  }

  .text-overlay {
    position: absolute;
    top: 35%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #242424;
    font-size: 18px;
    opacity: 0;
    transition: opacity 0.5s;
    width: 80%; 
    max-width: 90%; 
    padding: 10px;
  }

  .card:hover .text-overlay {
    opacity: 1;
  }

  .footer-page {
     text-align: center;
     margin-top: 30px; 
     padding: 20px;
     background-color: #f0f0f0;
     margin:auto; 
  }

  .footer-logo {
    width: 1000px; 
    height: 100px; 
    max-width: 1200px; 
    object-fit: fill; 
  }

  .footer-slogan {
     font-size: 18px;
     color: #333;
  }
</style>
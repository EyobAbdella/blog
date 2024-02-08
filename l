[1mdiff --git a/static/style.css b/static/style.css[m
[1mindex 3449b11..c5a878e 100644[m
[1m--- a/static/style.css[m
[1m+++ b/static/style.css[m
[36m@@ -1,3 +1,4 @@[m
[32m+[m[32m/* Global Styles */[m
 @import url("https://fonts.googleapis.com/css2?family=Roboto&display=swap");[m
 [m
 * {[m
[36m@@ -8,7 +9,6 @@[m
 }[m
 [m
 /* Article CSS */[m
[31m-[m
 .container {[m
   display: flex;[m
   justify-content: center;[m
[36m@@ -26,8 +26,7 @@[m
   height: 420px;[m
   max-width: 280px;[m
   border-radius: 10px;[m
[31m-  transition: box-shadow 0.3s ease;[m
[31m-  transition: transform 0.5s ease;[m
[32m+[m[32m  transition: box-shadow 0.3s ease, transform 0.5s ease;[m
   box-shadow: rgba(0, 0, 0, 0.02) 0px 1px 3px 0px,[m
     rgba(27, 31, 35, 0.15) 0px 0px 0px 1px;[m
 }[m
[36m@@ -77,13 +76,13 @@[m
 @media only screen and (max-width: 600px) {[m
   .card-header img {[m
     border-radius: 0;[m
[32m+[m[32m    border-radius: 10px;[m
   }[m
 }[m
 [m
 .user {[m
   display: flex;[m
   height: 50px;[m
[31m-  /* border: 1px solid black; */[m
   align-items: center;[m
   gap: 8px;[m
   padding: 0 4px;[m
[36m@@ -95,8 +94,7 @@[m
   border-radius: 50%;[m
 }[m
 [m
[31m-/* navbar CSS */[m
[31m-[m
[32m+[m[32m/* Navbar CSS */[m
 nav {[m
   color: #ccc;[m
   display: flex;[m
[36m@@ -125,8 +123,7 @@[m [mnav a {[m
   object-fit: contain;[m
 }[m
 [m
[31m-/* auth page */[m
[31m-[m
[32m+[m[32m/* Auth Page */[m
 .auth-container {[m
   display: flex;[m
   justify-content: center;[m
[36m@@ -141,6 +138,7 @@[m [mnav a {[m
 .auth-login {[m
   height: 80vh;[m
 }[m
[32m+[m
 .auth-signup {[m
   height: 100vh;[m
   padding-bottom: 2rem;[m
[36m@@ -161,6 +159,7 @@[m [ma {[m
 label {[m
   font-size: 11pt;[m
 }[m
[32m+[m
 #forgot-pass {[m
   color: #2dbd6e;[m
   font-family: "Raleway", sans-serif;[m
[36m@@ -168,6 +167,7 @@[m [mlabel {[m
   margin-top: 3px;[m
   text-align: right;[m
 }[m
[32m+[m
 #auth-card {[m
   border-radius: 8px;[m
   max-height: 600px;[m
[36m@@ -186,6 +186,7 @@[m [mlabel {[m
 #card-content {[m
   padding: 12px 44px;[m
 }[m
[32m+[m
 #card-title {[m
   font-family: "Raleway Thin", sans-serif;[m
   letter-spacing: 4px;[m
[36m@@ -193,6 +194,7 @@[m [mlabel {[m
   padding-top: 13px;[m
   text-align: center;[m
 }[m
[32m+[m
 #signup {[m
   color: #2dbd6e;[m
   font-family: "Raleway", sans-serif;[m
[36m@@ -200,6 +202,7 @@[m [mlabel {[m
   margin-top: 16px;[m
   text-align: center;[m
 }[m
[32m+[m
 #submit-btn {[m
   background: -webkit-linear-gradient(right, #a6f77b, #2dbd6e);[m
   border: none;[m
[36m@@ -214,25 +217,30 @@[m [mlabel {[m
   transition: 0.25s;[m
   width: 153px;[m
 }[m
[32m+[m
 #submit-btn:hover {[m
   box-shadow: 0px 1px 18px #24c64f;[m
 }[m
[32m+[m
 .form {[m
   display: flex;[m
   align-items: left;[m
   flex-direction: column;[m
 }[m
[32m+[m
 .form-border {[m
   background: -webkit-linear-gradient(right, #a6f77b, #2ec06f);[m
   height: 1px;[m
   width: 100%;[m
 }[m
[32m+[m
 .form-content {[m
   /* background: #fbfbfb; */[m
   border: none;[m
   outline: none;[m
   padding-top: 10px;[m
 }[m
[32m+[m
 .underline-title {[m
   background: -webkit-linear-gradient(right, #a6f77b, #2ec06f);[m
   height: 2px;[m
[36m@@ -268,6 +276,7 @@[m [mlabel {[m
 .detail-content {[m
   padding: 10px 100px;[m
 }[m
[32m+[m
 .detail-header {[m
   color: #ccc;[m
   padding: 20px 100px 100px 100px;[m
[36m@@ -313,7 +322,6 @@[m [mlabel {[m
 }[m
 [m
 /* Footer */[m
[31m-[m
 footer {[m
   margin-top: 2rem;[m
   min-height: 300px;[m
[36m@@ -330,7 +338,6 @@[m [mfooter {[m
 @media only screen and (max-width: 768px) {[m
   footer {[m
     padding: 10px;[m
[31m-    justify-content: center;[m
   }[m
 }[m
 [m
[36m@@ -346,8 +353,15 @@[m [mfooter p {[m
   text-align: center;[m
 }[m
 [m
[32m+[m[32m@media only screen and (max-width: 700px) {[m
[32m+[m[32m  .service {[m
[32m+[m[32m    width: 100%;[m
[32m+[m[32m    margin-top: 1rem;[m
[32m+[m[32m  }[m
[32m+[m[32m}[m
[32m+[m
 .service ul li {[m
[31m-  text-align: start;[m
[32m+[m[32m  text-align: center;[m
   list-style: none;[m
   margin-top: 8px;[m
 }[m
[36m@@ -382,4 +396,15 @@[m [mfooter p {[m
   gap: 8px;[m
   padding-left: 1rem;[m
   margin-top: 10px;[m
[32m+[m[32m  justify-content: center;[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32m.contact {[m
[32m+[m[32m  margin-top: 1rem;[m
[32m+[m[32m}[m
[32m+[m
[32m+[m[32m@media only screen and (max-width: 768px) {[m
[32m+[m[32m  .contact {[m
[32m+[m[32m    width: 100%;[m
[32m+[m[32m  }[m
 }[m
[1mdiff --git a/templates/footer.html b/templates/footer.html[m
[1mindex 9d53a18..14cab49 100644[m
[1m--- a/templates/footer.html[m
[1m+++ b/templates/footer.html[m
[36m@@ -22,7 +22,7 @@[m
       <li>Content Management Systems (CMS)</li>[m
     </ul>[m
   </div>[m
[31m-  <div>[m
[32m+[m[32m  <div class="contact">[m
     <p>Connect With Us</p>[m
     <div class="connect-icons">[m
       <a href="https://www.facebook.com/eyob.tashome.3" title="Facebook">[m

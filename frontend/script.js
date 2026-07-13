async function predict(){


let data = {

Age:Number(document.getElementById("age").value),

Tenure:Number(document.getElementById("tenure").value),

Total_Spend:Number(document.getElementById("spend").value),

Contract_Length:Number(document.getElementById("contract").value)

};



let response = await fetch(
"/predict",
{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

});


let result = await response.json();



document.getElementById("result").innerHTML =

"Churn Prediction : " + result.churn_prediction
+
"<br>"
+
"Result : " + result.message;


}
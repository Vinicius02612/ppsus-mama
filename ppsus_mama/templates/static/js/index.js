
function validateForm()
{
  bError=false
  var checkError=" "
  let q1,q2,q3,q4,q5,q7,q8,q9,q10,q11,q12,q13,q14
  q1=document.mainForm.nomePaciente.value
  if( q1=="" )
  {
    bError=true
    checkError=checkError + "question 2 is not a valid answer\n"
  }
  q2=document.mainForm.sobrenome.value
  if(isNaN(q2)||q2==null || q2=="" || parseInt(q2)<0 || parseInt(q2)>100 )
  {
    bError=true
    checkError=checkError + "question 2 is not a valid answer\n"
  }
  q3=document.mainForm.mutacao.value
  if(isNaN(q3)|| q3==null ||  q3=="" )
  {
    bError=true
    checkError=checkError + "question 3 is not a valid answer\n"
  }
    q4=document.mainForm.opcao_bilateral.value
  if(isNaN(q4)|| q4==null || q4=="" )
  {
    bError=true
    checkError=checkError + "question 4 is not a valid answer\n"
  }
  q5=document.mainForm.opcao_ovario.value
  if(isNaN(q5)|| q5==null ||  q5=="" )
  {
    bError=true
    checkError=checkError + "question 5 is not a valid answer\n"
  }
    q7=document.mainForm.cancer_mama.value
  if(isNaN(q7)|| q7==null ||  q7=="" )
  {
    bError=true
    checkError=checkError + "question 7 is not a valid answer\n"
  }
    q8=document.mainForm.cancer_diagnostio.value
  if(isNaN(q8)|| q8==null ||  q8=="" )
  {
    bError=true
    checkError=checkError + "question 8 is not a valid answer\n"
  }
    q9=document.mainForm.cancer_histologico.value
  if(isNaN(q9)|| q9==null ||  q9=="" )
  {
    bError=true
    checkError=checkError + "question 10 is not a valid answer\n"
  }
  q10=document.mainForm.tipo_molecular.value
  if(isNaN(q10)|| q10==null ||  q10=="" )
  {
    bError=true
    checkError=checkError + "question 10 is not a valid answer\n"
  }
  q11=document.mainForm.tam_cancer.value
  if(isNaN(q11)|| q11==null ||  q11=="" )
  {
    bError=true
    checkError=checkError + "question 10 is not a valid answer\n"
  }
  q12=document.mainForm.qtd_parent_1.value
  if(isNaN(q12)|| q12==null ||  q12=="" )
  {
    bError=true
    checkError=checkError + "question 10 is not a valid answer\n"
  }
  q13=document.mainForm.qtd_parent_2.value
  if(isNaN(q13)|| q13==null || q13=="" )
  {
    bError=true
    checkError=checkError + "question 10 is not a valid answer\n"
  }
  q14=document.mainForm.asc_judia.value
  if(isNaN(q14)|| q14==null || q14=="" )
  {
    bError=true
    checkError=checkError + "question 10 is not a valid answer\n"
  }
  if (bError)
  {
    alert(checkError)
  }
  else
  {
    document.mainForm.submit()
  }
}

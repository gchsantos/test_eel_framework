function js_test_func(){
    console.log("Worked!")
}
async function calculate(op, n1, n2){
    let result = await eel.calculate(op, n1, n2)();
    document.getElementById('result').value = result;
}

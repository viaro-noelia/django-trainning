function printData(){
    var divToPrint=document.getElementById("general-table");
    newWin= window.open("");
    newWin.document.write(divToPrint.outerHTML);
    newWin.print();
    newWin.close();
    }

$('#imprimir').on('click',function(){
    console.log('Imprimiendo')
    printData();
})
document.addEventListener('DOMContentLoaded', () =>{
    const options = {
        chart: {
            type: 'column',
            zoomTypr: 'xy'
        },
        title: {
            text: 'Word analysis'
        },
        yAxis: {
            title: {
                text: 'number'
            }
        },
    }; 
    $.get('Analysed.csv', csv =>{
       options.data = {
        csv
       } ;
       Highcharts.chart('container',options);
    });
    
});
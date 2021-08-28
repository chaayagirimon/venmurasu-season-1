document.addEventListener('DOMContentLoaded', () =>{
    const options = {
        chart: {
            type: 'column',
            zoomTypr: 'xy'
        },
        title: {
            text: 'Word Count'
        },
        yAxis: {
            title: {
                text: 'number of words'
            }
        }
    }; 
    $.get('Completed_Final.csv', csv =>{
       options.data = {
        csv
       } ;
       Highcharts.chart('container',options);
    });
    
});
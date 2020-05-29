$(function(){
    var statuschart = new Chart(document.getElementById('crdrchart'), {
      type: 'doughnut',
      data: {
                labels: ["Debit","Credit"],
                datasets: [{
                    label: "",
                    backgroundColor: ["#333399", "#c6c6ec"],
                      data: [50.50,261.50],
                }]
            },
      options: {
        responsive: true,
        cutoutPercentage: 60,
        title: {
            display: false,
            text: 'Status'
          },
        legend: {
        display: false,
            position:'right',
        },
        onClick:function(e){
            try {
                var dict = {
                  0: "passed",
                  1: "failed",
                  2: "skipped",
                  3: "broken",
                };
                var activePoints = statuschart.getElementsAtEvent(e);
                var selectedIndex = activePoints[0]._index;
                var status=selectedIndex;
                display_other_page();
                filterSelection(dict[status]);
            }
            catch(err) {}
        }
       },
    });
});

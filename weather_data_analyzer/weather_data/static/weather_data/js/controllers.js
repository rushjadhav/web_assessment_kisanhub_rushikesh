weatherApp.controller('indexController', function($scope) {

    console.log("indexController")

});

weatherApp.controller('regionController', function($scope, $http, $routeParams){

    $scope.regionId = $routeParams.id;
    $scope.monthlyWeather = [];

    var config = {
        params: {'region_id' : $scope.regionId},
    };

    $http.get('/api/monthly_weathers', config).then(function(response) {
        $scope.monthlyWeather = response.data
        $scope.regionName = $scope.monthlyWeather[0].region_name
        $scope.hideLoader()
    });

    $scope.hideLoader = function(){
        document.getElementById("loader").style.display = "none";
    };
});

weatherApp.controller('dashboardController', function($scope, $http) {

    $scope.regions = []
    $scope.interestingFacts = []

    $http.get('/api/interesting_facts/').then(function(response){
        $scope.interestingFacts = response.data
    });

    $http.get('/api/regions').then(function(response) {
        $scope.regions = response.data
        $scope.selectedRegion = $scope.regions[0]
        $scope.drawGraph()
    });

    $scope.drawGraph = function(){
      var averageMonthly = document.getElementById('averageMonthlyData').getContext('2d');
      
      var chart = new Chart(averageMonthly, {
        type: 'line',
        data: {
          labels: ["January", "February", "March", "April", "May", "June", "July",
                   "August", "September", "Octomber", "November", "December"],
          datasets: [{
              label: "Average Max Temperature",
              borderColor: 'rgba(153, 102, 255, 1)',
              data: $scope.selectedRegion.average_max_temperature_monthwise,
            },
            {
              label: "Average Min Temperature",
              borderColor: 'rgba(255,99,132,1)',
              data: $scope.selectedRegion.average_min_temperature_monthwise,
            },
            {
              label: "Average Mean Temperature",
              borderColor: 'rgba(54, 162, 235, 1)',
              data: $scope.selectedRegion.average_mean_temperature_monthwise,
            },
            {
              label: "Average Rainfall",
              borderColor: 'rgba(255, 206, 86, 1)',
              data: $scope.selectedRegion.average_rainfall_monthwise,
            },
            {
              label: "Average Sunshine",
              borderColor: 'rgba(75, 192, 192, 1)',
              data: $scope.selectedRegion.average_sunshine_monthwise,
            }
          ]
        },
      });
    }
});
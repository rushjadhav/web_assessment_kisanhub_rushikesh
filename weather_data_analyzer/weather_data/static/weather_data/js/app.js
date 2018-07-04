var weatherApp = angular.module('weatherApp', ['ngRoute']);

//To resolve confilct between django and angularjs template
weatherApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});

weatherApp.config(function($routeProvider) {

    $routeProvider.when('/', {
        templateUrl : '/static/weather_data/templates/dashboard.html',
        controller  : 'dashboardController'
    }).when('/region/:id', {
        templateUrl : '/static/weather_data/templates/region.html',
        controller  : 'regionController'
    })

});

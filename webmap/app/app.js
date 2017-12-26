import '../node_modules/angular/angular.min.js';
import '../node_modules/angular-route/angular-route.js';
// import '../node_modules/jquery/dist/jquery.min.js';
// import '../node_modules/maphilight/jquery.maphilight.min.js';
import './app.css';
import './overview/overview.js';

// Declare app level module which depends on views, and components
angular.module('houseApp', [
  'ngRoute',
  'houseApp.overview'
]).
config(['$locationProvider', '$routeProvider', function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');

  $routeProvider.otherwise({redirectTo: '/overview'});
}]);

weatherApp.filter('stringToDate',function ($filter){
    return function (ele, dateFormat){
        return $filter('date')(new Date(ele),dateFormat);
    }
})

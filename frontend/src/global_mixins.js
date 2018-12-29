export const globalMixin = {
    /**
     * File where all re-usable functions for different functions are put.
     * This is loaded in main js and available in every component through out the app
     * */
    // Load all the sub mixins
    mounted: function () {
    },
    methods: {
        ajaxPromise(param) {
            /**
             * This is generalized ajax call function, which takes param values and returns promise.
             * It handles error by opening a notification box.
             * @param: {param} A dict containing url, type of request and data as key
             * */
            let contentType = 'application/json;charset=utf-8'
            if ("contentType" in param) {
                contentType = param.contentType
            }
            const self = this;
            return new Promise(function (resolve, reject) {
                $.ajax({
                    url: param.url,
                    beforeSend(request) {
                    },
                    type: param.type,
                    data: param.data,
                    processData: false,
                    contentType: contentType,
                    cache: false,
                    success(data) {
                        if (data) {
                            resolve(data);
                        } else {
                            resolve(true);
                        }
                    },
                    error(errorData) {
                        console.log('Error', errorData)
                        reject(errorData)
                    }
                });
            })
        }
    }
}

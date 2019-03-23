export default
    methods:
        notifySuccess: (msg) ->
            this.$message({
                title: 'Success',
                message: msg,
                type: 'success',
                customClass: 'notificationBanner',
                duration: 3000,
                showClose: true
            })

        notifyError: (msg) ->
            this.$message({
                title: 'Error',
                message: msg,
                customClass: 'notificationBanner',
                type: 'error',
                duration: 3000,
                showClose: true   
            })

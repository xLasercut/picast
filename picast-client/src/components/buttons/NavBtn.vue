<template>
    <v-btn text @click="$emit('click')" v-bind="$attrs" v-on="activator">
        <v-icon>
            {{icon}}
        </v-icon>
    </v-btn>
</template>

<script lang="ts">
    import {createComponent} from '@vue/composition-api'

    export default createComponent({
        props: {
            activator: {},
            icon: {
                type: String
            }
        }
    })
</script>

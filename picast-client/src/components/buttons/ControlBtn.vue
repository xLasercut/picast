<template>
    <v-btn depressed v-bind="$attrs" @click="$emit('click')">
        <v-icon>
            <slot></slot>
        </v-icon>
    </v-btn>
</template>

<script lang="ts">
    import {createComponent} from '@vue/composition-api'

    export default createComponent({})
</script>

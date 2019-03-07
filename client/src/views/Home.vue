<template>
	<el-main class="home">
		<el-row>
			<el-input></el-input>
		</el-row>
		<el-row>
			<el-slider v-model="videoPosition" show-input></el-slider>
		</el-row>
		<el-row>
			<el-col :span="10">
				<el-button><font-awesome-icon :icon="playbackStatus"/></el-button>
				<el-button><font-awesome-icon icon="stop"/></el-button>
				<el-button><font-awesome-icon icon="step-backward"/></el-button>
				<el-button><font-awesome-icon icon="step-forward"/></el-button>
			</el-col>
			<el-col :span="4">
				<el-slider v-model="volume" show-input></el-slider>
			</el-col>
		</el-row>
		<el-row>
			
		</el-row>
	</el-main>
</template>

<script>
	import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
	export default {
		components: {
			FontAwesomeIcon
		},
		data () {
			return {
				playbackStatus: "play",
				volume: 100,
				videoPosition: 0
			}
		},
		methods: {
			
		}
	}
</script>

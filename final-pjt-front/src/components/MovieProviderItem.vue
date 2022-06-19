<template>
<li class="mr-2">
  <a :href=path.provider_path target='_blank' class="provider">
    <img v-if="this.path.provider_id==8" src="@/assets/provider_logo/8.jpg" title="Watch on Netflix" alt="Button to Netflix">
    <img v-if="this.path.provider_id==96" src="@/assets/provider_logo/96.jpg" title="Watch on Naver" alt="Button to Naver">
    <img v-if="this.path.provider_id==97" src="@/assets/provider_logo/97.jpg" title="Watch on Watcha" alt="Button to Watcha">
    <img v-if="this.path.provider_id==119" src="@/assets/provider_logo/119.jpg" title="Watch on Amazon" alt="Button to Amazon">
    <img v-if="this.path.provider_id==337" src="@/assets/provider_logo/337.jpg" title="Watch on Disney" alt="Button to Disney">
    <img v-if="this.path.provider_id==350" src="@/assets/provider_logo/350.jpg" title="Watch on Apple" alt="Button to Apple">
    <img v-if="this.path.provider_id==356" src="@/assets/provider_logo/356.jpg" title="Watch on Wavve" alt="Button to Wavve">
  </a>
</li>
</template>

<script>
export default {
  name: 'MovieProviderItem',
  props: {
    path: Object,
  },
  data() {
    return {
      isHovered: false
    }
  },
  methods: {
    handleHover(hovered) {
      this.isHovered = hovered
    }
  }
}
</script>

<style scoped>
img {
  width: 3rem;
  border-radius: 1rem
}
</style>
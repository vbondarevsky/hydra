<template>
  <div class="about">
    <h1>This is an about page</h1>


  <ul>
    <li v-for="node in nodes" :key="node.id">
      {{ node }}
    </li>
  </ul>

  </div>
</template>

<script>
  import { mapState } from 'vuex'

  export default {
      mounted() {
          this.$store.dispatch('loadNodes')
      },
      computed: {
          ...mapState([
              'nodes'
          ])
      }
  }
</script>

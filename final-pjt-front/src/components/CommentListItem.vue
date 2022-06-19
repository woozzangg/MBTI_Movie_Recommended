<template>
<div>
  <b-row class="d-flex justify-content-between pb-3">
    <b-col cols="2" >
      <router-link class="font-weight-bold text-dark pr-3" :to="{ name: 'profile', params: { username: comment.user.username } }">
        {{ comment.user.username }}
      </router-link>
    </b-col>
    <b-col cols="7" class="d-flex">
      <div>
        <p class="mb-0 pb-0" v-if="!isEditing">{{ payload.content }}</p>
        <p class="mb-0 pb-0" v-if="isEditing"><input type="text" v-model="payload.content"></p>
      </div>

      <div v-if="isEditing">
        <b-button @click="onUpdate" variant="light" size="sm">Update</b-button>
        <b-button @click="switchIsEditing" size="sm">Cancel</b-button>
      </div>
    </b-col>
    <b-col cols="3" class="d-flex justify-content-end my-1">
      <b-container>
        <b-row class="d-flex justify-content-end">
          <small v-if="comment.created_at === comment.updated_at">{{ (comment.created_at+'').substr(0,10) +' ' + (comment.created_at+'').substr(11,8) }}</small>
          <small v-if="comment.created_at !== comment.updated_at">{{ '(수정됨) ' + (comment.updated_at+'').substr(0,10) +' ' + (comment.updated_at+'').substr(11,8) }} </small>
        </b-row>
        <b-row class="d-flex justify-content-end">
          <span v-if="currentUser.username === comment.user.username && !isEditing" class="d-flex justify-content-end">
            <b-button @click="switchIsEditing" variant="light" size="sm">Edit</b-button> 
            <b-button @click="deleteComment(payload)" size="sm">Delete</b-button>
          </span>
        </b-row>
      </b-container>
    </b-col>
    
  </b-row>
  <hr>
</div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 1px solid green;

}
</style>
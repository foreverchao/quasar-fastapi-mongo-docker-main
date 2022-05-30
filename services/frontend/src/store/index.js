import Vuex from 'vuex'

export default new Vuex.Store({
  state: {
    token: null,
  },
  mutations: {
    updateToken(state, value) {
      state.token = value;
    },
  },
  actions: {
  },
  modules: {
  }
})

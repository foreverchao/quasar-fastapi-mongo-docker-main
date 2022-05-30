<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title> Cros Dashboard </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item clickable v-ripple to="/">
            <q-item-section avatar>
              <q-icon name="home" />
            </q-item-section>

            <q-item-section>
                Home
            </q-item-section>
        </q-item>
      </q-list>

      <q-list  class="rounded-borders" dense>
        <q-expansion-item :content-inset-level="0.5" expand-separator icon="list" label="System Management">
            <q-item to="/systemManagement/userManagment" clickable v-ripple :header-inset-level="1">
              <q-item-section avatar>
                <q-icon name="perm_identity" />
              </q-item-section>

              <q-item-section>
                  User Management
              </q-item-section>
        </q-item>
        </q-expansion-item>
      </q-list>

      <q-list>
        <q-item clickable v-ripple @click="Logout">
            <q-item-section avatar>
              <q-icon name="exit_to_app" />
            </q-item-section>

            <q-item-section>
                Logout
            </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",

  components: {
    
  },
  mounted() {
      this.initialize();
  },

  

  setup() {
    const leftDrawerOpen = ref(false);
    return {
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },

  methods: {

    initialize(){
      
      if(!this.$q.sessionStorage.has("token")) this.$router.push("/login");
      if (this.$q.sessionStorage.getItem("token") == "") this.$router.push("/login"); else console.log(this.$q.sessionStorage.getItem("token"));

    },
    
    Logout(){  
      
      this.$q.sessionStorage.set("token", "")
      this.$router.push('/login')
    }

  }
});
</script>

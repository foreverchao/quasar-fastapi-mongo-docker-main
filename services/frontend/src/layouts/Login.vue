<template>
    <q-layout view="lHh Lpr lFf">
        <q-page-container>
        <q-page class="bg-light-blue-4 window-height window-width row justify-center items-center">
            <div class="column">
            <div class="row">
                <h5 class="text-h5 text-white q-my-md">Cros Dashboard</h5>
            </div>
            <div class="row">
                <q-card square bordered class="q-pa-lg shadow-1">
                <q-card-section>
                    <q-form class="q-gutter-md">
                    <q-input square filled clearable v-model="form.email" type="email" label="email"  />
                    <q-input square filled clearable v-model="form.password" type="password" label="password"  />
                    </q-form>
                </q-card-section>
                <q-card-actions class="q-px-md">
                    <q-btn unelevated  @click="Login" color="light-blue-7" size="lg" class="full-width" label="Login" />
                </q-card-actions>
                <q-card-section class="text-center q-pa-none">
                    <!-- <p class="text-grey-6">Not reigistered? Created an Account</p> -->
                </q-card-section>
                </q-card>
            </div>
            </div>
        </q-page>
        </q-page-container>
    </q-layout>
</template>

<script>
import {apiUserLogin} from "src/api/auth";

export default {
    name: 'Login',
    data () {
        return {
        form: {
            email: '',
            password: ''
        }
        }
    },
    created(){
    },

    mounted() {
      this.initialize();
    },
    
    methods: {

        initialize(){
            if(this.$q.sessionStorage.has("token"))
                if (this.$q.sessionStorage.getItem("token") != "") this.$router.push("/");
        },
        
        Login(){
            
            apiUserLogin(this.form)
            .then((res) => {

                this.$q.sessionStorage.set("token", res.data.access_token)
                this.$router.push("/");
                
            })
            .catch((err) => {
                //console.log(err.response) 
            });


        },

        


    }
}
</script>

<style>
.q-card {
  width: 360px;
}
</style>

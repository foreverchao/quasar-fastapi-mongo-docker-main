<template>
<div class="q-pa-md">
    <div class="q-pa-md">
        <q-btn color="primary" label="Add New User" icon="add" @click="isDialog = true"  />
    </div>
    <div id="q-app" style="min-height: 100vh;">
        <div class="q-pa-md">
            <q-table
                title="Users List"
                :rows="data"
                :columns="columns"
                row-key="name"
                :filter="filter"
            >

                <template v-slot:top-right>
                    <q-input borderless dense debounce="300" v-model="filter" placeholder="Search" clearable>
                        <q-icon  name="search" />
                    </q-input>
                </template>
                <template v-slot:body="props">
                    <q-tr :props="props">
                        <q-td key="name" :props="props">
                            <q-input v-model="props.row.name" filled type="text" :dense="dense" readonly></q-input>
                        </q-td>
                        <q-td key="email" :props="props">
                            <q-input v-model="props.row.email" filled type="email" :dense="dense" readonly></q-input>
                            
                            
                        </q-td>
                        
                        <q-td key="actions" :props="props" >
                            <div class="q-px-md q-gutter-sm">
                                <q-btn left color="green"  name="edit" label='edit' icon='edit'  @click="editItem(props.row)"></q-btn>
                                <q-btn left color="red"  name="delete" label='delete' icon='delete'  @click="deleteItem(props.row)"></q-btn>
                                <!-- <q-btn right color="red"  name="permission" label='permission' icon='person_add' ></q-btn> -->
                            </div>
                        </q-td>
                    </q-tr>
                </template>
            </q-table>

            <q-dialog v-model="isDialog">
                <q-card style="width: 700px; max-width: 80vw;"> 
                    <q-card-section>
                        <div class="text-h6">{{ formTitle }}</div>
                    </q-card-section>

                    <q-card-section style="max-height: 50vh" class="scroll">
                        <div class="q-gutter-md row items-start">
                            <q-input v-model="editedItem.name"  filled type="text" label="Name" ></q-input>
                            <q-input v-if="editedIndex == -1"  v-model="editedItem.email" filled type="email" label="Email" ></q-input>
                            <q-input v-if="editedIndex != -1" readonly v-model="editedItem.email" filled type="email" label="Email" ></q-input>
                            <q-input v-if="editedIndex == -1" v-model="editedItem.password"  filled type="password" label="Password" ></q-input>
                        </div>
                    </q-card-section>
                    
                    <q-card-actions align="right">
                        <q-btn flat label="OK" color="primary" v-close-popup @click="addItem" ></q-btn>
                    </q-card-actions>
                </q-card>
            </q-dialog>

        </div>
    </div>
</div>
</template>

<script>
import {apiUserSignup,apiAllUserGet,apiUserPut,apiUserDelete} from "src/api/users";
const columns = [
  {
    name: 'name',
    required: true,
    label: 'Name',
    align: 'center',
    field: row => row.name,
    format: val => `${val}`,
    sortable: true
  },
  
  { name: 'email', align: 'center',label: 'Email', field: 'email', sortable: true },
  { name: 'actions', align: 'center',label: 'Actions', field: 'actions' }
]



export default {
    
    data() {
        return {
            columns,
            data:[],
            isDialog: false,
            filter:'',
            editedIndex: -1,
            editedItem: {
                name: "",
                email: "",
            },
            defaultItem: {
                name: "",
                email: "",
                password:"",
            }
        }
    },

    
    components: {
        
    },
    mounted() { 
        this.initialize();
    },

    watch:{
        isDialog (val) {
            val || this.close()
        },
    },

    computed: {
        formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
        },
    },

    methods: {

        initialize(){
            apiAllUserGet()
            .then((res)=>{   
                for (var i=0; i<res.data.length; i++){
                    var temp ={
                        name: res.data[i].name,
                        email: res.data[i].email,
                        id: res.data[i]._id
                    }
                    this.data.push(temp);
                }
            }
            ).catch((err)=>{
                console.error(err)
            })
        },


        editItem(item) {
            this.editedIndex = this.data.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.isDialog = true
        },
        addItem(){
            if (this.editedIndex > -1) {
                Object.assign(this.data[this.editedIndex], this.editedItem);
                apiUserPut(
                    this.editedItem.id,
                    {
                        "name": this.editedItem.name,
                        "role": [
                            "Admin"
                        ],
                        "updatedAt": this.getNowDate()
                    }
                )
                .then((res)=>{
                    console.log(res);
                    this.$router.go()
                })
                .catch((err) => {
                        console.log(err)
                });

            } else {
                apiUserSignup(
                    {
                        "name": this.editedItem.name,
                        "email": this.editedItem.email,
                        "password": this.editedItem.password,
                        "role": [
                            ""
                        ]
                    }
                )
                .then((res) => {
                    console.log(res)
                    this.$router.go()
                })
                .catch((err) => {
                    console.log(err) 
                });
            }
            this.close()
            
        },
        deleteItem(item) {
            this.editedItem = Object.assign({}, item)
            if (this.data.length == 1) {
                this.$q.notify({
                    message: 'Can not delete last account.',
                    color: 'red',
                    type:'negative',
                    position:'top',
                })
            }
            else{
                this.$q.notify({
                message: 'Make sure you want to delete.',
                color: 'red',
                type:'negative',
                position:'top',
                actions: [
                        { label: 'Accept', color: 'yellow', handler: () => { 
                                apiUserDelete(this.editedItem.id)
                                .then((res) => {console.log(res)},this.$router.go())
                                .catch((err) => {console.log(err)}) 
                            } 
                        },
                        { label: 'Cancel', color: 'white', handler: () => { /* ... */ } }
                    ]
                })
            }
            
            
        },
        close () {
            this.isDialog = false
            setTimeout(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            }, 300)
        },
        getNowDate(){
            var today = new Date();
            return today.toISOString()
        },
        

        
    }
}
</script>

const routes = [
  {
    path: "/",
    component: () => import("layouts/Home.vue"),
    children: [{ path: "", component: () => import("pages/Index.vue") }],
  },

  {
    path: '/login',
    component: () => import('layouts/Login.vue'),
    children: [{
        path: '',
        component: () => import('pages/Index.vue')
    }]
  },
  {
    path: '/systemManagement',
    component: () => import('layouts/Home.vue'),
    children: [
        {
            path: 'userManagment',
            component: () => import('pages/systemManagement/userManagement.vue')
        }
    ]
},

  // Always leave this as last one,
  // but you can also remove it
  // {
  //   path: "/:catchAll(.*)*",
  //   component: () => import("pages/Error404.vue"),
  // },
];

export default routes;

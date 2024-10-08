import {createRouter, createWebHashHistory} from 'vue-router';
import {isLoginedUser} from "../utils/token.js";
import {showMessage} from "../utils/message.js";

const routes = [
    {
        path: '/',
        name: 'Main',
        component: () => import('../views/main/MainView.vue'),
        meta:{
            title: '首页'
        },
        children: [
            {
                path: '/',
                name: 'MainIndex',
                component: () => import('../views/main/index/MainIndex.vue'),
                meta:{
                    title: '首页'
                }
            },
            {
                path: '/blog/categories',
                name: 'MainBlogCategories',
                component: () => import('../views/main/blog/BlogCategories.vue'),
                meta:{
                    title: '文章类型'
                }
            },
            {
                path: '/resource/categories',
                name: 'MainResourceCategories',
                component: () => import('../views/main/resource/ResourceCategories.vue'),
                meta:{
                    title: '资源类型'
                }
            },
            {
                path: '/testcase/product',
                name: 'MainTestCasesProducts',
                component: () => import('../views/main/testcase/Products.vue'),
                meta:{
                    title: '测试产品'
                }
            },
            {
                path: '/bugs/dashboard',
                name: 'MainBugsDashboard',
                component: () => import('../views/main/bug/BugsDashboard.vue'),
                meta:{
                    title: '缺陷看板'
                }
            },
            {
                path: '/home/index',
                name: 'MainHomeIndex',
                component: () => import('../views/user/UserHomeView.vue'),
                meta:{
                    title: '我的主页'
                },
                children: [
                    {
                        path: '/home/index',
                        name: 'MainHomeIndex',
                        component: () => import('../views/user/home/HomeIndex.vue'),
                        meta:{
                            title: '主页看板'
                        },
                    },
                    {
                        path: '/home/notifications',
                        name: 'MainHomeNotifications',
                        component: () => import('../views/user/home/Notifications.vue'),
                        meta:{
                            title: '我的通知'
                        },
                    },
                ]
            },
            {
                path: '/user/settings/profile',
                name: 'MainUserSettings',
                component: () => import('../views/user/UserSettingView.vue'),
                meta:{
                    title: '基本设置'
                },
                children: [
                    {
                        path: '/user/settings/profile',
                        name: 'MainUserChangeProfile',
                        component: () => import('../views/user/settings/ChangeProfile.vue'),
                        meta:{
                            title: '基本设置'
                        },
                    },
                    {
                        path: '/user/settings/change-avatar',
                        name: 'MainUserChangeAvatar',
                        component: () => import('../views/user/settings/ChangeAvatar.vue'),
                        meta:{
                            title: '修改头像'
                        },
                    },
                ]
            },
        ]
    },
    {
        path: '/admin',
        name: 'Admin',
        component: () => import('../views/admin/AdminView.vue'),
        children: [
            {
                path: '/admin',
                name: 'AdminIndex',
                component: () => import('../views/admin/index/AdminIndex.vue'),
            }
        ]
    },
    {
        path: '/auth/login',
        name: 'AuthLogin',
        component: () => import('../views/auth/Login.vue'),
    },
    {
        path: '/forbidden',
        name: 'Forbidden',
        component: () => import('../views/errors/403.vue'),
    },
    {
        path: '/error',
        name: 'serverError',
        component: () => import('../views/errors/500.vue'),
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'notFound',
        component: () => import('../views/errors/404.vue'),
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes: routes,
});


// 路由拦截器
// router.beforeEach((to, from, next) => {
//     if (to.path.startsWith('/admin')) {
//         if (isLoginedUser()) {
//             next()
//         } else {
//             next('/auth/login')
//         }
//     } else {
//         next()
//     }
// })


// router.beforeEach((to, from, next) => {
//     // 如果用户已经登录
//     if (isLoginedUser()) {
//         // 如果用户访问登录页面
//         if (to.path === '/auth/login') {
//             showMessage('warning', '您已经处于登陆状态')
//             // 跳转到首页
//             next('/')
//         } else {
//             // 否则放行
//             next()
//         }
//     } else {
//         if (to.path === '/auth/login') {
//             next()
//         } else {
//             next('/auth/login')
//         }
//     }
// })


export default router

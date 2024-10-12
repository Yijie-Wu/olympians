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

                    {
                        path: '/home/tests',
                        name: 'MainHomeTests',
                        component: () => import('../views/user/home/Tests.vue'),
                        meta:{
                            title: '我的测试'
                        },
                    },
                    {
                        path: '/home/testcases',
                        name: 'MainHomeTestcases',
                        component: () => import('../views/user/home/TestCases.vue'),
                        meta:{
                            title: '我的用例'
                        },
                    },
                    {
                        path: '/home/bugs',
                        name: 'MainHomeBugs',
                        component: () => import('../views/user/home/Bugs.vue'),
                        meta:{
                            title: '我的缺陷'
                        },
                    },
                    {
                        path: '/home/blogs',
                        name: 'MainHomeBlogs',
                        component: () => import('../views/user/home/Blogs.vue'),
                        meta:{
                            title: '我的文章'
                        },
                    },
                    {
                        path: '/home/videos',
                        name: 'MainHomeVideos',
                        component: () => import('../views/user/home/Videos.vue'),
                        meta:{
                            title: '我的视频'
                        },
                    },
                    {
                        path: '/home/apps',
                        name: 'MainHomeApps',
                        component: () => import('../views/user/home/Apps.vue'),
                        meta:{
                            title: '我的程序'
                        },
                    },
                    {
                        path: '/home/books',
                        name: 'MainHomeBooks',
                        component: () => import('../views/user/home/Books.vue'),
                        meta:{
                            title: '我的书籍'
                        },
                    },
                    {
                        path: '/home/tools',
                        name: 'MainHomeTools',
                        component: () => import('../views/user/home/Tools.vue'),
                        meta:{
                            title: '我的工具'
                        },
                    },
                    {
                        path: '/home/reports',
                        name: 'MainHomeReports',
                        component: () => import('../views/user/home/Reports.vue'),
                        meta:{
                            title: '我的报告'
                        },
                    },
                    {
                        path: '/home/pictures',
                        name: 'MainHomePictures',
                        component: () => import('../views/user/home/Pictures.vue'),
                        meta:{
                            title: '我的图片'
                        },
                    },
                ]
            },
            {
                path: '/user/settings/profile',
                name: 'MainUserSettings',
                component: () => import('../views/user/UserSettingView.vue'),
                meta:{
                    title: '设置'
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
                    {
                        path: '/user/settings/change-password',
                        name: 'MainUserChangePassword',
                        component: () => import('../views/user/settings/ChangePassword.vue'),
                        meta:{
                            title: '修改密码'
                        },
                    },
                    {
                        path: '/user/settings/tokens',
                        name: 'MainUserTokens',
                        component: () => import('../views/user/settings/Tokens.vue'),
                        meta:{
                            title: '令牌列表'
                        },
                    },
                    {
                        path: '/user/settings/test-settings',
                        name: 'MainUserTestSettings',
                        component: () => import('../views/user/settings/TestSettings.vue'),
                        meta:{
                            title: '测试设置'
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

<script setup>
import {ref, computed} from 'vue'
import {Search, Postcard, View, MoreFilled} from "@element-plus/icons-vue";

import LogoSVG from '../../../assets/images/playwright.svg'
import AppImage from '../../../assets/images/app.jpeg'
import LogsImage from '../../../assets/images/logs.jpg'
import BooksImage from '../../../assets/images/books.jpeg'
import ToolsImage from '../../../assets/images/tools.jpeg'
import ReportImage from '../../../assets/images/report.jpeg'
import PictureImage from '../../../assets/images/picture.jpg'
import FilesImage from '../../../assets/images/files.jpg'
import VideoImage from '../../../assets/images/video.jpg'

const searchText = ref('')

</script>

<template>
  <div class="resources-category-container">
    <div class="resources-category-header">
      <el-input
          v-model="searchText"
          size="large"
          :prefix-icon="Postcard"
          :suffix-icon="Search"
          placeholder="搜索资源类型"
      />
    </div>
    <div class="resources-category-body">
      <el-row :gutter="0">
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="VideoImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">视频</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="AppImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">软件</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="ToolsImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">工具</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="BooksImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">书籍</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="FilesImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">文件</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="ReportImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">报告</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="PictureImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">图片</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :md="8">
          <el-card class="resource-category-container">
            <div style="height: 100px;display: flex;box-sizing: border-box;">
              <div
                  style="display: flex;align-items: center;justify-content: center;width:100px;height:100px;box-sizing: border-box;">
                <el-avatar :src="LogsImage" :size="100" shape="square"/>
              </div>
              <div style="margin-left: 15px;flex: 1;">
                <div style="display: flex;align-items: center;">
                  <div style="flex: 1;height: 30px;">
                    <el-text truncated style="font-size: 20px;font-weight: bold;">日志</el-text>
                  </div>
                  <div style="width: 80px;height: 30px;display: flex;align-items: center;justify-content: center;">
                    <el-icon>
                      <MoreFilled/>
                    </el-icon>
                  </div>
                </div>
                <div style="margin-top: 6px;">
                  <el-tag type="success" round size="small">Python库</el-tag>
                  <el-tag type="success" round style="margin-left: 5px;" size="small">UI自动化</el-tag>
                </div>
                <div style="margin-top: 10px;display: flex;align-items: center;">
                  <el-avatar :src="LogoSVG" :size="25" style="border: 1px solid silver;"/>
                  <el-avatar
                      :src="LogoSVG"
                      v-for="i in 10"
                      :style="{ border: '1px solid silver', left: `${-8 * i}px`, position: 'relative' }"
                      :size="25"
                  />
                  <el-avatar :src="LogoSVG" :size="25"
                             style="border: 1px solid silver;position: relative;left: -88px;"/>
                </div>
              </div>
            </div>
            <div style="width: 100%;height: 60px;margin-top: 10px;">
              Playwright 是一个著名的UI自动化框架, 为UI自动化提供了丰富的API和代码录制工具
            </div>
            <div style="width: 100%;height: 40px;display: flex;align-items: center;">
              <div style="flex: 1">
                <el-text truncated type="primary">100篇文章, 最后更新于: 三天前</el-text>
              </div>
              <div style="width: 80px;display: flex;align-items: center;justify-content: flex-end;">
                <el-button type="success" round :icon="View" size="small">查看</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<style scoped>
.resources-category-container {
  height: calc(100vh - 70px);
  box-sizing: border-box;
  margin: 5px 0;
  display: flex;
  flex-direction: column;
  overflow-y: scroll;
}

.resources-category-header {
  height: 50px;
  /*background: linear-gradient();*/
  background-color: #3d444c;
  width: 90%;
  margin: 5px auto;
  padding: 0 20px;
  border-radius: 25px;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: center;
}

.resources-category-body {
  width: 90%;
  margin: 5px auto;
  overflow-y: auto;
  box-sizing: border-box;
  padding: 0;
}

.resource-category-container {
  height: 240px;
  box-sizing: border-box;
  padding: 0;
  margin: 2px;
}


</style>

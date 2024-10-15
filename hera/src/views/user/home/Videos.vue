<script setup>
import {computed, ref} from 'vue'
import {Search} from "@element-plus/icons-vue";

const search = ref('')
const select = ref('')
const noti_type = ref(true)
const tableHeight = window.innerHeight - 160
// const filterTableData = computed(() =>
//     tableData.filter(
//         (data) =>
//             !search.value ||
//             data.name.toLowerCase().includes(search.value.toLowerCase())
//     )
// )
const handleEdit = (index, row) => {
  console.log(index, row)
}
const handleDelete = (index, row) => {
  console.log(index, row)
}

const tableData = [
  {
    type: '系统',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    type: '测试',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    type: '系统',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
]
</script>

<template>
  <div class="item-container">
    <div class="item-header">
      <div style="display: flex;align-items: center;flex: 1;">
        <div style="flex: 1;">
          <el-input
              v-model="search"
              placeholder="请输入视频标题"
          >
            <template #prepend>
              <el-select v-model="select" placeholder="选择类型" style="width: 115px">
                <el-option label="测试视频" value="1"/>
                <el-option label="文章视频" value="2"/>
                <el-option label="个人视频" value="3"/>
                <el-option label="所有视频" value="4"/>
              </el-select>
            </template>
            <template #append>
              <el-button :icon="Search"/>
            </template>
          </el-input>
        </div>
      </div>
      <div style="width: 100px;display: flex;align-items: center;justify-content: flex-end;">
        <el-button type="danger" round plain>全部删除</el-button>
      </div>
    </div>
    <div class="item-body">
      <el-table :data="tableData" border style="width: 100%" :height="tableHeight">
        <el-table-column label="类型" prop="type" width="100" fixed="left" align="center"/>
        <el-table-column label="消息" prop="name"/>
        <el-table-column align="center" label="常规操作" width="200">
          <template #default="scope">
            <el-button size="small" round type="success" plain @click="handleEdit(scope.$index, scope.row)">
              查看
            </el-button>
            <el-button size="small" round type="warning" plain @click="handleEdit(scope.$index, scope.row)">
              编辑
            </el-button>
            <el-button
                size="small"
                type="danger"
                round
                plain
                @click="handleDelete(scope.$index, scope.row)"
            >
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="item-footer">
      <el-pagination
          size="small"
          background
          layout="prev, pager, next"
          :total="50"
          class="mt-4"
      />
    </div>
  </div>

</template>


<style scoped>
.item-container {
  margin: 5px 10px;
  border: 1px solid #3d444c;
  height: calc(100vh - 70px);
  display: flex;
  flex-direction: column;
  border-radius: 5px;
}

.item-header {
  height: 40px;
  margin-bottom: 5px;
  border-bottom: 1px solid #3d444c;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 10px;
}

.item-body {
  flex: 1;
  margin: 0 2px;
}

.item-footer {
  height: 40px;
  border-top: 1px solid #3d444c;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 10px;
}

</style>

<script setup>
import {computed, ref} from 'vue'

const search = ref('')
const tableHeight = window.innerHeight - 130
const filterTableData = computed(() =>
    tableData.filter(
        (data) =>
            !search.value ||
            data.name.toLowerCase().includes(search.value.toLowerCase())
    )
)
const handleEdit = (index, row) => {
  console.log(index, row)
}
const handleDelete = (index, row) => {
  console.log(index, row)
}

const tableData = [
  {
    date: '2016-05-03',
    name: 'Tom',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-02',
    name: 'John',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-04',
    name: 'Morgan',
    address: 'No. 189, Grove St, Los Angeles',
  },
  {
    date: '2016-05-01',
    name: 'Jessy',
    address: 'No. 189, Grove St, Los Angeles',
  },
]
</script>

<template>
  <div class="item-container">
    <div class="item-header">
      <div>1</div>
      <div>2</div>
    </div>
    <div class="item-body">
      <el-table :data="filterTableData" border style="width: 100%" :height="tableHeight">
        <el-table-column label="Date" prop="date"/>
        <el-table-column label="Name" prop="name"/>
        <el-table-column align="center" label="常规操作" width="150" >
          <template #default="scope">
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
  height: 50px;
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

</style>

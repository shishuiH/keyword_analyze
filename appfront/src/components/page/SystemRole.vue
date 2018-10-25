<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-lx-people"></i> 用户管理 </el-breadcrumb-item>
                <el-breadcrumb-item>系统用户</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container" style="padding: 35px;">
            <div class="handle-box">

                 <el-button type="primary" icon="delete" class="handle-del mr10" @click="handleSignBatch">批量标记</el-button>

                <el-input v-model.trim="select_word" placeholder="筛选关键词" class="handle-input mr10" @keyup.enter.native="handleSearch"></el-input><!--@keyup.enter.native监听回车键-->
                <el-button type="primary" icon="el-icon-search" @click="handleSearch" >搜索</el-button>

                <el-button type="primary" icon="el-icon-edit" @click="handleAddRole">增加  角色</el-button>
            </div>
            <el-table :data="tableData" border class="table" ref="multipleTable" @selection-change="handleSelectionChange">
                <el-table-column type="selection" width="55" align="center"></el-table-column>
               <el-table-column prop="id" label="id" v-show="true" sortable width="150">
                </el-table-column>
                <el-table-column prop="role_name" label="角色昵称">
                </el-table-column>
                <el-table-column prop="update_date" label="最新修改时间" sortable>
                </el-table-column>
                <el-table-column label="操作" align="center">
                    <template slot-scope="scope">
                        <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button type="text" icon="el-icon-delete" class="red" @click="handleDelete(scope.row)">删除</el-button>
                        <!--<el-button type="text" icon="" @click="handleSign(scope.row)">标记已读</el-button>-->
                    </template>
                </el-table-column>
            </el-table>
            <div class="pagination">
                <el-col :span="24" class="toolbar pageBar">
                    <el-pagination background
                                   @current-change="handleCurrentChange"
                                   @size-change="handleSizeChange"
                                   :current-page="cur_page"
                                   :page-sizes="[10, 20, 50]"
                                   :page-size="page_size"
                                   layout="prev, pager, next, sizes, total"
                                   :total="total">
                    </el-pagination>
                </el-col>
            </div>
        </div>


         <!-- 增加弹出框 -->
        <el-dialog title="增加  角色" :visible.sync="addVisible" width="30%" >
            <el-form ref="add_role_form" :model="add_role_form" label-width="100px">
                <el-form-item label="角色昵称" prop="role_name">
                    <el-input v-model="add_role_form.role_name" @keyup.enter.native="addRole" ></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="callOf('add_role_form')">取 消</el-button>
                <el-button type="primary" @click="addRole('add_role_form')">确 定</el-button>
            </span>
        </el-dialog>


        <!-- 编辑弹出框 -->
        <el-dialog title="编辑" :visible.sync="editVisible" width="30%">
            <el-form ref="form" :model="form" label-width="100px">
                <el-form-item label="id" prop="id" v-show="false">
                    <el-input v-model="form.id"></el-input>
                </el-form-item>
                <el-form-item label="角色昵称" prop="role_name">
                    <el-input v-model="form.role_name" @keyup.enter.native="saveEdit"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="callOf1('form')">取 消</el-button>
                <el-button type="primary" @click="saveEdit">确 定</el-button>
            </span>
        </el-dialog>


        <!-- 删除提示框 -->
        <el-dialog title="提示" :visible.sync="delVisible" width="300px" center>
            <div class="del-dialog-cnt">删除不可恢复，是否确定删除？</div>
            <span slot="footer" class="dialog-footer">
                <el-button @click="delVisible = false">取 消</el-button>
                <el-button type="primary" @click="deleteRow">确 定</el-button>
            </span>
        </el-dialog>


    </div>
</template>

<script>
    import { getRoles, delRole, signBatch } from "../../api/role_api";
    export default {
        name: 'role_table',
        data() {
            return {
                total: 0,
                page: 1,
                page_size: 10,
                page_num: 1,
                url: '',
                tableData: [],
                cur_page: 1,
                multipleSelection: [],
                select_cate: '',
                select_word: '',
                del_list: [],
                sign_list: [],
                is_search: false,
                addVisible:false,
                editVisible: false,
                delVisible: false,
                form: {
                    id: '',
                    role_name: '',
                },
                add_role_form : {
                    role_name: '',
                },
                idx: -1
            }
        },
        created() {
            this.getData();
        },
        computed: {
            data() {
                return this.tableData.filter((d) => {
                    let is_del = false;
                    for (let i = 0; i < this.del_list.length; i++) {
                        if (d.name === this.del_list[i].name) {
                            is_del = true;
                            break;
                        }
                    }
                    if (!is_del) {
                        if (d.address.indexOf(this.select_cate) > -1 &&
                            (d.name.indexOf(this.select_word) > -1 ||
                                d.address.indexOf(this.select_word) > -1)
                        ) {
                            return d;
                        }
                    }
                })
            }
        },
        methods: {
            // 分页导航
            //点击当前页码
            handleCurrentChange(val) {
                this.page_num = val;
                this.getData();
            },
            //改变页面大小
            handleSizeChange(val) {
                this.page_size = val;
                this.getData();
            },

            // 获取 easy-mock 的模拟数据
            getData() {

               getRoles({
                   page_num: this.page_num,
                   page_size: this.page_size,
                   select_word : this.select_word
               }).then((res) => {

                   if (res.data.code === 200) {

                       this.total = res.data.total;  //后台返回的数据总记录数
                       // this.cur_page = res.data.cur_page;   //如果有需要可以定位当前页
                       this.tableData = res.data.list;  //回显集合
                   } else {
                       this.$message.error(res.data.e)
                   }

                }).catch(error => {
                    console.log('出错了');
                    console.log(error);
                })
            },
            search() {
                this.is_search = true;
            },
            /*formatter(row, column) {
                return row.address;
            },*/
            filterTag(value, row) {
                return row.tag === value;
            },
            handleEdit(index, row) {

                this.form = Object.assign({}, {
                    id: row.id,
                    role_name: row.role_name,
                })
                this.editVisible = true;
            },
            //将id赋值给idx,弹出提示框
            handleDelete( row ) {
                this.idx = row.id;
                this.delVisible = true;
            },
            /*delAll() {
                const length = this.multipleSelection.length;
                let str = '';
                this.del_list = this.del_list.concat(this.multipleSelection);
                for (let i = 0; i < length; i++) {
                    str += this.multipleSelection[i].name + ' ';
                }
                this.$message.error('删除了' + str);
                this.multipleSelection = [];
            },*/
            handleSignBatch() {

                const length = this.multipleSelection.length;

                if (length <= 1) {

                    this.$message.info('请至少选择一行记录');
                    return;
                }
                let str = '';
                this.sign_list = this.sign_list.concat(this.multipleSelection);
                let ids = [];
                for (let i = 0; i < length; i++) {
                    // str += this.multipleSelection[i].id + ',';
                    ids.push(this.multipleSelection[i].id);
                }
                // console.log('删除了' + str);
                this.multipleSelection = [];    //数组重新置空

                //求请后台
                signBatch({
                    ids : ids
                }).then((res) => {

                  if (res.data.code === 200) {

                      this.$message.success(res.data.msg);
                      this.getData();
                   } else {
                       this.$message.error(res.data.e)
                   }

                }).catch(error => {

                    console.log(error);
                })
            },
            handleSelectionChange(val) {
                this.multipleSelection = val;
            },
            // 保存编辑
            addRole(form_name) {

               console.log('add role');
               this.$axios.post('/createRole/', JSON.stringify(this.add_role_form)).then(res => {
                   if (res.data.code == 200) {

                       this.getData();
                   } else {
                       this.$message.error(`出错了`)
                   }
               }).catch(error => {

                   this.$message.error(error);
               })

                //关闭弹窗
               this.addVisible = false;
               this.$refs[form_name].resetFields();
            },
            //取消增加角色
            callOf(form_name) {

                this.addVisible = false;
                this.$refs[form_name].resetFields();
            },
            //取消增加角色
            callOf1(form_name) {

                this.editVisible = false;
                this.$refs[form_name].resetFields();
            },
            // 保存编辑
            saveEdit() {

               console.log('update role');
               this.$axios.post('/updateRole/', JSON.stringify(this.form)).then(res => {
                   if (res.data.code == 200) {

                       this.getData();
                   } else {
                       this.$message.error(`出错了`)
                   }
               }).catch(error => {

                   this.$message.error(error);
               })

                this.editVisible = false;
                this.$message.success(`修改成功`);
            },
            // 请求后台，确定删除
            deleteRow(){

                if(-1 == this.idx)
                    return;
                delRole({
                    id: this.idx,
                }).then((res) => {

                     if (res.data.code == 200) {

                       this.getData();
                   } else {
                       this.$message.error(`出错了`)
                   }

                }).catch(error => {
                    console.log(error);
                })

                this.$message.success('删除成功');
                this.delVisible = false;

            },
            //关键词搜索
            handleSearch(){

                searchMessageList({
                    page_num: this.page_num,
                    page_size: this.page_size,
                    select_word : this.select_word
                }).then((res) => {

                   if (res.data.code === 200) {
                       //console.log(res.data.list);
                       this.total = res.data.total;
                       // this.cur_page = res.data.cur_page;   //如果有需要可以定位当前页
                       this.tableData = res.data.list;
                   } else {
                       this.$message.error(res.data.e)
                   }

                }).catch(error => {
                    console.log('出错了');
                    console.log(error);
                })
            },
            handleAddRole() {

                this.addVisible = true;
            }
        }
    }

</script>

<style scoped>
    .handle-box {
        margin-bottom: 20px;
    }

    .handle-select {
        width: 120px;
    }

    .handle-input {
        width: 300px;
        display: inline-block;
    }
    .del-dialog-cnt{
        font-size: 16px;
        text-align: center
    }
    .table{
        width: 100%;
        font-size: 14px;
    }
    .red{
        color: #ff0000;
    }
</style>

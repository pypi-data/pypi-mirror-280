import os
import sys

file_path = os.path.abspath(__file__)
end = file_path.index('mns') + 17
project_path = file_path[0:end]
sys.path.append(project_path)

import mns_scheduler.risk.major_violations.register_and_investigate_stock_sync_api \
    as register_and_investigate_stock_sync_api
from loguru import logger
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import mns_scheduler.dt.stock_dt_pool_sync as stock_dt_pool_sync_api
import mns_scheduler.zb.stock_zb_pool_sync as stock_zb_pool_sync_api
import mns_common.component.trade_date.trade_date_common_service_api as trade_date_common_service_api
import mns_common.utils.date_handle_util as date_handle_util
import mns_scheduler.k_line.sync.daily_week_month_line_sync as daily_week_month_line_sync_api
import mns_common.utils.ip_util as ip_util
import mns_scheduler.db.col_move_service as col_move_service
import mns_scheduler.db.db_status as db_status_api
import mns_scheduler.big_deal.ths_big_deal_sync as ths_big_deal_sync_api
import mns_scheduler.zt.open_data.kcx_high_chg_open_data_sync as kcx_high_chg_open_data_sync
import mns_scheduler.zt.export.export_kcx_high_chg_open_data_to_excel as export_kcx_high_chg_open_data_to_excel
import mns_scheduler.zt.connected_boards.zt_five_boards_sync_api as zt_five_boards_sync_api
import mns_scheduler.zt.zt_pool.zt_pool_sync_api as zt_pool_sync_api
import mns_scheduler.k_line.clean.k_line_info_clean_task as k_line_info_clean_service
import mns_scheduler.concept.clean.ths_concept_clean_api as ths_concept_choose_api
import mns_common.api.em.east_money_stock_gdfx_free_top_10_api as east_money_stock_gdfx_free_top_10_api
import \
    mns_scheduler.concept.ths.update_concept_info.sync_one_concept_all_symbols_api as sync_one_concept_all_symbols_api
import \
    mns_scheduler.concept.ths.update_concept_info.sync_one_symbol_all_concepts_api as sync_one_symbol_all_concepts_api
import mns_scheduler.kpl.selection.total.sync_kpl_best_total_sync_api as sync_kpl_best_total_sync_api
import mns_scheduler.company_info.base.sync_company_base_info_api as company_info_sync_api
import mns_scheduler.trade.auto_ipo_buy_api as auto_ipo_buy_api
import mns_scheduler.kpl.selection.index.sync_best_choose_his_index as sync_best_choose_his_index
import mns_scheduler.concept.ths.common.ths_concept_update_common_api as ths_concept_update_common_api
import mns_scheduler.trade.sync_position_api as sync_position_api
import mns_scheduler.concept.clean.kpl_concept_clean_api as kpl_concept_clean_api
import mns_scheduler.company_info.de_list_stock.de_list_stock_service as de_list_stock_service
import mns_scheduler.irm.stock_irm_cninfo_service as stock_irm_cninfo_service
import mns_scheduler.open.sync_one_day_open_data_to_db_service as sync_one_day_open_data_to_db_service
import mns_scheduler.zt.high_chg.sync_high_chg_pool_service as sync_high_chg_pool_service
import mns_scheduler.zt.high_chg.sync_high_chg_real_time_quotes_service as sync_high_chg_real_time_quotes_service
import mns_scheduler.risk.self.wei_pan_stock_api as wei_pan_stock_api
import mns_scheduler.risk.transactions.transactions_check_api as transactions_check_api
import mns_scheduler.concept.ths.sync_new_index.sync_ths_concept_new_index_api as sync_ths_concept_new_index_api
import mns_scheduler.company_info.clean.company_info_clean_api as company_info_clean_api


# 同步交易日期任务完成
def sync_trade_date():
    trade_date_common_service_api.sync_trade_date()
    logger.info('同步交易日期任务完成')


# 跌停信息
def sync_stock_dt_pool():
    now_date = datetime.now()
    str_now_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_now_day):
        stock_dt_pool_sync_api.sync_stock_dt_pool(str_now_day)
        logger.info("同步跌停信息任务执行成功:{}", str_now_day)


# 炸板信息
def sync_stock_zb_pool():
    now_date = datetime.now()
    str_now_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_now_day):
        stock_zb_pool_sync_api.sync_stock_zb_pool(str_now_day)
        logger.info("同步跌停信息任务执行成功:{}", str_now_day)


# 定时同步每周交易行情数据(前复权)
def stock_sync_qfq_weekly():
    now_date = datetime.now()
    str_now_date = now_date.strftime('%Y-%m-%d')
    if date_handle_util.last_day_of_week(now_date):
        logger.info('同步每周行情数据(前复权):' + str_now_date)
        daily_week_month_line_sync_api.sync_all_daily_data('weekly', 'qfq', 'stock_qfq_weekly', None)


# # 定时同步每周交易行情数据(前复权)
def stock_sync_qfq_monthly():
    now_date = datetime.now()
    str_now_date = now_date.strftime('%Y-%m-%d')
    if date_handle_util.last_day_month(now_date):
        logger.info('同步每周行情数据(前复权):' + str_now_date)
        daily_week_month_line_sync_api.sync_all_daily_data('monthly', 'qfq', 'stock_qfq_monthly',
                                                           None)


#  当天实时数据备份
def col_data_move():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    logger.info('当天实时数据备份:{}', str_day)
    if trade_date_common_service_api.is_trade_day(str_day):
        mac_address = ip_util.get_mac_address()
        if mac_address is not None and mac_address == ip_util.WINDOWS_MAC_ADDRESS_CD:
            col_move_service.sync_col_move(str_day)
        else:
            # 删除最早一天数据
            col_move_service.delete_exist_data(str_day)


# db 状态check
def db_status_check():
    db_status_api.db_status_check()


# 同步大单数据
def sync_ths_big_deal():
    now_date = datetime.now()
    str_now_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_now_day):
        logger.info('更新大单数据')
        ths_big_deal_sync_api.sync_ths_big_deal(False)


# 定时同步每日交易行情数据(前复权)
def stock_daily_sync_qfq():
    now_date = datetime.now()
    str_now_date = now_date.strftime('%Y-%m-%d')
    logger.info('同步每日行情数据(前复权):' + str_now_date)
    daily_week_month_line_sync_api.sync_all_daily_data('daily',
                                                       'qfq', 'stock_qfq_daily', None)


# 同步当日k c x 高涨幅数据
def realtime_quotes_now_zt_kc_data_sync():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_day):
        # 同步当日kcx 高涨幅 当天交易数据和开盘数据
        kcx_high_chg_open_data_sync.sync_all_kc_zt_data(str_day, None)
        # 同步当日开盘数据
        sync_one_day_open_data_to_db_service.sync_one_day_open_data(str_day)
        # 涨停数据同步到excel
        export_kcx_high_chg_open_data_to_excel.export_kc_zt_data(str_day)


# 同步涨停池
def sync_stock_zt_pool():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_day):
        logger.info('同步当天涨停池股开始')
        stock_zt_pool = zt_pool_sync_api.save_zt_info(str_day)
        zt_five_boards_sync_api.update_five_connected_boards_task(stock_zt_pool)
        logger.info('同步当天涨停池股票完成')


# 保存今天高涨幅数据
def sync_toady_stock_zt_pool():
    logger.info('同步今天涨幅大于9.5的symbol')
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    # 同步高涨幅实时行情
    sync_high_chg_real_time_quotes_service.sync_high_chg_real_time_quotes(str_day)
    # 同步高涨幅列表
    sync_high_chg_pool_service.sync_stock_high_chg_pool_list(str_day, None)


# 计算下一个交易日k线数据
def generate_new_day_k_line_info():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    # 生成下一个交易日日期k线数据 number=2 获取下一个交易日 日期
    next_trade_day = trade_date_common_service_api.get_further_trade_date(str_day, 2)
    k_line_info_clean_service.sync_k_line_info_task(next_trade_day)
    logger.info('计算当日k线信息完成:{}', str_day)


# 同步一天k线 涨停 数据
def sync_daily_data_info():
    # 同步k线数据
    try:
        stock_daily_sync_qfq()
    except BaseException as e:
        logger.error("同步当日k线数据异常:{}", e)

    # 同步当日k c x 高涨幅数据
    try:
        realtime_quotes_now_zt_kc_data_sync()
    except BaseException as e:
        logger.error("同步当日kcx高涨幅数据异常:{}", e)

    # 同步涨停池数据信息
    try:
        sync_stock_zt_pool()
    except BaseException as e:
        logger.error("同步涨停数据信息异常:{}", e)

    # 同步今日高涨幅数据 依赖涨停股票池的数据
    try:
        sync_toady_stock_zt_pool()
    except BaseException as e:
        logger.error("同步今日高涨幅数据异常:{}", e)

    # 计算当日k线数据
    try:
        generate_new_day_k_line_info()
    except BaseException as e:
        logger.error("计算当日k线数据异常:{}", e)


# 同步当天交易k线数据
def sync_today_trade_k_line_info():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_day):
        k_line_info_clean_service.sync_k_line_info_task(str_day)
        logger.info('计算当日k线信息完成:{}', str_day)


# 同步所有股票前十大流通股本
def sync_stock_gdfx_free_top_10_one_day():
    logger.info('同步所有股票前十大流通股本')
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    east_money_stock_gdfx_free_top_10_api.sync_stock_gdfx_free_top_10_one_day(str_day)


# 更新概念信息
def concept_info_clean():
    #  更新空概念名称
    ths_concept_choose_api.update_null_name()
    #  更新概念包含个数
    ths_concept_choose_api.update_ths_concept_info()
    # 开盘啦概念信息更新
    kpl_concept_clean_api.update_kpl_concept_info()


# 同步概念下所有股票组成 by 概念指数
def update_concept_all_detail_info():
    logger.info('同步概念下所有股票组成')
    sync_one_concept_all_symbols_api.update_concept_all_detail_info()
    ths_concept_update_common_api.update_ths_concept_choose_null_reason()


# 同步单只股票下所有概念 by 股票代码
def update_one_symbol_all_concepts():
    logger.info('同步单只股票所有概念组成')
    sync_one_symbol_all_concepts_api.sync_symbol_all_concept(None)
    ths_concept_update_common_api.update_ths_concept_choose_null_reason()


# 同步开盘啦精选指数
def sync_all_kpl_plate_info():
    logger.info('同步开盘啦精选指数开始')
    sync_kpl_best_total_sync_api.sync_all_plate_info()


# 更新一二级关系
def update_best_choose_plate_relation():
    logger.info('同步开盘啦精选指数关系')
    sync_kpl_best_total_sync_api.update_best_choose_plate_relation()


# 同步ths新概念
def sync_new_concept_index():
    sync_ths_concept_new_index_api.sync_ths_concept_new_index()
    logger.info("同步ths新概念任务完成")

    ths_concept_update_common_api.update_ths_concept_choose_null_reason()
    logger.info("更新空的入选概念任务完成")


# 同步ths新概念 轮训任务
def sync_new_concept_index_task():
    now_date = datetime.now()
    hour = now_date.hour
    if hour != 9:
        sync_ths_concept_new_index_api.sync_ths_concept_new_index()
        logger.info("同步ths新概念任务完成")


# 清洗公司基本信息
def update_company_base_info():
    company_info_sync_api.sync_company_base_info(None)
    company_info_clean_api.fix_company_industry(None)
    # 退市股票同步
    de_list_stock_service.sync_de_list_stock()
    logger.info('同步公司基本信息任务完成')


# 自动打新
def auto_ipo_buy():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    if trade_date_common_service_api.is_trade_day(str_day):
        auto_ipo_buy_api.auto_ipo_buy()


# 同步持仓
def sync_position():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    # 同步持仓
    if trade_date_common_service_api.is_trade_day(str_day):
        logger.info('同步持仓任务完成')
        sync_position_api.sync_position()


# 同步开盘啦当日精选指数行情数据

def sync_kpl_best_his_quotes():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    last_trade_day = trade_date_common_service_api.get_last_trade_day(str_day)
    if trade_date_common_service_api.is_trade_day(last_trade_day):
        sync_best_choose_his_index.sync_best_choose_his_index(last_trade_day)
        logger.info('同步开盘啦当日精选指数行情数据任务完成')


# 同步高风险的股票
def sync_high_risk_stocks():
    logger.info('同步被立案调查的股票')
    register_and_investigate_stock_sync_api.sync_register_and_investigate_stocks()
    reason_detail = '微盘股拉黑'
    concept_code_wei_pan = '883418'
    wei_pan_stock_api.add_concept_to_lack_list(concept_code_wei_pan, reason_detail)
    logger.info('同步交易类风险的股票')
    transactions_check_api.transactions_check_task()


# 同步互动回答
def sync_all_interactive_questions():
    now_date = datetime.now()
    str_day = now_date.strftime('%Y-%m-%d')
    hour = now_date.hour
    tag = (bool(1 - trade_date_common_service_api.is_trade_day(str_day))) or (hour >= 17)
    if tag:
        logger.info('同步互动回答')
        stock_irm_cninfo_service.sync_all_interactive_questions(None)


# # 定义BlockingScheduler
blockingScheduler = BlockingScheduler()
# sync_trade_date 同步交易日期
blockingScheduler.add_job(sync_trade_date, 'cron', hour='20', minute='43')

# 跌停信息同步
blockingScheduler.add_job(sync_stock_dt_pool, 'cron', hour='15,17,21,03,07', minute='37')

# 炸板信息同步
blockingScheduler.add_job(sync_stock_zb_pool, 'cron', hour='15,17,21,03,07', minute='55')

# (前复权--周k线)
blockingScheduler.add_job(stock_sync_qfq_weekly, 'cron', day_of_week='fri', hour=16, minute=20)

# (前复权--月k线)
blockingScheduler.add_job(stock_sync_qfq_monthly, 'cron', hour='15,18', minute='35')

# 数据备份
blockingScheduler.add_job(col_data_move, 'cron', hour='15', minute='33')

# 数据库健康检查
blockingScheduler.add_job(db_status_check, 'interval', seconds=30, max_instances=4)

# 同步大单数据 暂停同步 20240430
# blockingScheduler.add_job(sync_ths_big_deal, 'cron', hour='09', minute='30', max_instances=4)

# todo 需要前后顺序执行
# todo 当日k线信息
# 同步一天k线 涨停 数据
blockingScheduler.add_job(sync_daily_data_info, 'cron', hour='15,20', minute='26')

# 开盘前同步当天交易需要的k线数据
blockingScheduler.add_job(sync_today_trade_k_line_info, 'cron', hour='08', minute='30')

# 同步十大流通股东信息
blockingScheduler.add_job(sync_stock_gdfx_free_top_10_one_day, 'cron', hour='08,22', minute='23')

# 更新同花顺概念信息
blockingScheduler.add_job(concept_info_clean, 'cron', hour='9,12,20', minute='24')

# 更新概念指数下所有股票组成 by 概念代码
blockingScheduler.add_job(update_concept_all_detail_info, 'cron', hour='08,18,12', minute='30')

# 同步单只股票下所有概念 by 股票代码
blockingScheduler.add_job(update_one_symbol_all_concepts, 'cron', hour='09,18,12', minute='15')

# 开盘前同步同花顺新概念指数
blockingScheduler.add_job(sync_new_concept_index, 'cron', hour='09,22', minute='01,10,20,28,41,58')

# 同步同花顺新增概念指数(定时轮训,暂时10分钟)
blockingScheduler.add_job(sync_new_concept_index_task, 'interval', minutes=10, max_instances=4)

# 同步开盘啦新增精选概念(定时轮训,暂时五分钟)
blockingScheduler.add_job(sync_all_kpl_plate_info, 'interval', minutes=5, max_instances=4)

# 同步公司基本信息
blockingScheduler.add_job(update_company_base_info, 'cron', hour='08,18', minute='05')
# 更新当天涨停股票池
blockingScheduler.add_job(sync_stock_zt_pool, 'cron', hour='15,19,21,23', minute='42')

# 自动打新 打新中签高时间段 10:30-11:30
blockingScheduler.add_job(auto_ipo_buy, 'cron', hour='10', minute='40,50')

# 更新开盘啦指数关系
blockingScheduler.add_job(update_best_choose_plate_relation, 'cron', hour='09,18', minute='25')

# 更新开盘啦指数关系
blockingScheduler.add_job(sync_kpl_best_his_quotes, 'cron', hour='18,22', minute='25')

# 更新开盘啦指数关系
blockingScheduler.add_job(sync_position, 'cron', hour='0,08', minute='10')

# 同步高风险股票
blockingScheduler.add_job(sync_high_risk_stocks, 'cron', hour='0,09,12,16', minute='20')

# 同步互动回答
blockingScheduler.add_job(sync_all_interactive_questions, 'cron', hour='08,12,17', minute='05')

print('定时任务启动成功')
blockingScheduler.start()
#
# if __name__ == '__main__':
#     col_data_move()

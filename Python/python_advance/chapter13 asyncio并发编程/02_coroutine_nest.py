# 1. run_until_complete
# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()
# loop.run_until_complete()


# 注册协程到loop中有两种方法
# 1. 通过ensure_future/create_task
# 2. await

# loop也会被放到future中,跳过future停掉    future放到loop
# 1-协程取消future(task)

# import asyncio
# import time
#
# async def get_html(sleep_times):
#     print("waiting")
#     await asyncio.sleep(sleep_times)
#     print("done after {}s".format(sleep_times))
#
#
# if __name__ == "__main__":
#     task1 = get_html(2)
#     task2 = get_html(3)
#     task3 = get_html(3)
#
#     tasks = [task1, task2, task3]
#
#     loop = asyncio.get_event_loop()
#
#     try:
#         loop.run_until_complete(asyncio.wait(tasks))
#     except KeyboardInterrupt as e:
#         all_tasks = asyncio.Task.all_tasks()
#         for task in all_tasks:
#             print("cancel task")
#             print(task.cancel())
#         loop.stop()
#         loop.run_forever()
#     finally:
#         loop.close()


# 2-协程嵌套
import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()

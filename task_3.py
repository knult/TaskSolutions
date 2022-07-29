"""
Provide a code fragment that switches the current browser to another tab (consider there are only 2 tabs).
Please comment on the code in detail.
"""

# Solution 1
#get current window handle
cur_handle = driver.current_window_handle
#get list all handles
all_tab = driver.window_handles

for tab in all_tab:
    # switch tab
    if tab != cur_handle:
        driver.switch_to.window(tab)
        break

# Solution 2
#get list all handles
all_tab = driver.window_handles
# remove current tab handle
all_tab.remove(driver.current_window_handle)
# all_tab will contain only one tab, go to it
driver.switch_to.window(all_tab[0])






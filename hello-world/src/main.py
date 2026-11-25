import flet as ft


def main(page: ft.Page):
    hello_world = ft.Text("Hello World", size=50)
    counter = ft.Text("0", size=50, data=0)

    # ＋を押したとき
    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)

    # −を押したとき
    def decrement_click(e):
        counter.data -= 1
        counter.value = str(counter.data)

    # 左に−、右に＋を配置
    page.floating_action_button = ft.Row(
        controls=[
            ft.FloatingActionButton(
                icon=ft.Icons.REMOVE,
                key="decrement",
                on_click=decrement_click,
            ),
            ft.FloatingActionButton(
                icon=ft.Icons.ADD,
                key="increment",
                on_click=increment_click,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # 文字とカウンターを表示
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=ft.Column(
                    controls=[hello_world, counter],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
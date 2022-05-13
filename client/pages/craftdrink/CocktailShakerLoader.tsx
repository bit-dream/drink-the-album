import styles from './cocktail.module.css'
import { Text, Center, Spacer, Flex, Box } from '@chakra-ui/react'

interface Shaker {
    gradient: string[]
}

const CocktailShakerLoader = (props) => {
    return(
        <Flex 
            justify='center' 
            align='center' 
            height='100vh'
            background={[
                `linear-gradient(to bottom, ${props.gradient[0]}, ${props.gradient[1]})`,
                `linear-gradient(to bottom, ${props.gradient[0]}, ${props.gradient[1]})`, 
                `linear-gradient(to right, ${props.gradient[0]}, ${props.gradient[1]})`,
                `linear-gradient(to right, ${props.gradient[0]}, ${props.gradient[1]})`
              ]}
            >
            <Box className={styles.shaker}>
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><g data-name="Outline"><path d="M58.05 44.771a1 1 0 001.322-.5 29.963 29.963 0 000-24.542 1 1 0 00-1.824.822 27.955 27.955 0 010 22.9A1 1 0 0058.05 44.771zM54 32a21.691 21.691 0 01-.611 5.133 1 1 0 101.943.474 23.866 23.866 0 000-11.214 1 1 0 10-1.943.474A21.691 21.691 0 0154 32zM5.95 44.771a1 1 0 00.5-1.322 27.955 27.955 0 010-22.9 1 1 0 00-1.824-.822 29.963 29.963 0 000 24.542A1 1 0 005.95 44.771zM9.877 38.342a1 1 0 00.734-1.209 21.867 21.867 0 010-10.266 1 1 0 10-1.943-.474 23.866 23.866 0 000 11.214A1 1 0 009.877 38.342zM20.631 35.717a1 1 0 00.992.886 1.088 1.088 0 00.114-.006 1 1 0 00.88-1.108l-.64-5.6a1 1 0 10-1.987.228z"/><path d="M15.6,26.96l3.5,30.607A5,5,0,0,0,24.069,62H39.931A5,5,0,0,0,44.9,57.568L48.4,26.96A2.994,2.994,0,0,0,51,24V23a2.994,2.994,0,0,0-2.188-2.874l-1.463-5.854A3,3,0,0,0,44.438,12H43.78l-.431-1.728A3,3,0,0,0,40.438,8H39.72l-.86-2.582A4.993,4.993,0,0,0,34.117,2H29.883a5,5,0,0,0-4.744,3.419L24.279,8h-.717a3,3,0,0,0-2.911,2.272L20.22,12h-.658a3,3,0,0,0-2.911,2.272l-1.463,5.854A2.994,2.994,0,0,0,13,23v1A2.994,2.994,0,0,0,15.6,26.96Zm27.46,29.053c-.022,0-.041-.013-.064-.013H28a1,1,0,0,0,0,2H42.752a2.994,2.994,0,0,1-2.821,2H24.069a3,3,0,0,1-2.981-2.66L17.62,27H46.38ZM27.036,6.051A3,3,0,0,1,29.883,4h4.234a3,3,0,0,1,2.847,2.051L37.613,8H26.387Zm-4.445,4.707A1,1,0,0,1,23.562,10H40.438a1,1,0,0,1,.971.758L41.72,12H22.28Zm-4,4A1,1,0,0,1,19.562,14H44.438a1,1,0,0,1,.971.758L46.72,20H17.28ZM15,23a1,1,0,0,1,1-1H48a1,1,0,0,1,1,1v1a1,1,0,0,1-1,1H16a1,1,0,0,1-1-1Z"/><circle cx="22" cy="39.5" r="1"/></g></svg>
            </Box>
        </Flex>
    )
}

export default CocktailShakerLoader